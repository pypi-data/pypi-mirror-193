import re
import asyncio
from pathlib import Path
from dataclasses import dataclass

from adb_shell.adb_device_async import AdbDeviceTcpAsync
from adb_shell.auth.sign_pythonrsa import PythonRSASigner
from adb_shell.auth.keygen import keygen
from adb_shell.exceptions import TcpTimeoutException

from googletv.constants import (
    ADB_MAX_RETRIES,
    ADB_RETRY_INTERVAL,
    ADB_MAX_TIMEOUTS,
    APP_ATV_LAUNCHER,
    APP_NETFLIX,
    APP_NLZIET,
    APP_PLEX,
    APP_TVHEADEND,
    APP_VLC,
    APP_YOUTUBE,
    APP_NAMES,
    CMD_DUMPSYS_ACTIVITY,
    CMD_DUMPSYS_DISPLAY,
    CMD_DUMPSYS_ERROR,
    CMD_DUMPSYS_MEDIA_SESSION,
    CMD_DUMPSYS_POWER,
    REGEX_ACTIVITY_RESUMED,
    REGEX_ACTIVITY,
    REGEX_ASLEEP,
    REGEX_AWAKE,
    REGEX_PLAYBACK_STATE,
    REGEX_SCREEN_OFF,
    REGEX_SCREEN_ON,
    REGEX_SESSION,
    REGEX_WAKE_LOCK_SIZE,
    STATE_IDLE,
    STATE_OFF,
    STATE_PAUSED,
    STATE_PLAYING,
)
from googletv.exception import GoogleTvException
from googletv.search import search_nested


class AdbKey:
    def __init__(self, file_path: str) -> None:
        self._file_path = file_path

        self._public_key: str | None = None
        self._private_key: str | None = None

    @property
    def public_key_path(self) -> str:
        return f"{self._file_path}.pub"

    @property
    def private_key_path(self) -> str:
        return self._file_path

    @property
    def public_key(self) -> str:
        if self._public_key is None:
            with open(f"{self._file_path}.pub", "r") as f:
                self._public_key = f.read()

        return self._public_key

    @property
    def private_key(self) -> str:
        if self._private_key is None:
            with open(self._file_path, "r") as f:
                self._private_key = f.read()

        return self._private_key

    @property
    def exists(self) -> bool:
        for path in (self.private_key_path, self.public_key_path):
            if not Path(path).is_file():
                return False

        return True

    @staticmethod
    def generate(file_path: str) -> "AdbKey":
        keygen(file_path)
        return AdbKey(file_path)


@dataclass(frozen=True)
class DeviceState:
    awake: bool | None = None
    screen_on: bool | None = None
    app: str | None = None
    playback_state: str | None = None


class GoogleTv:
    def __init__(self, adb_key: AdbKey, host: str, port: int = 5555) -> None:
        self._adb = AdbDeviceTcpAsync(host, port)
        self._adb_key = adb_key

        self._state = DeviceState()
        self._timeout_counter = 0

    @property
    def available(self) -> bool:
        return self._adb.available

    @property
    def state(self) -> DeviceState:
        return self._state

    async def connect(self) -> None:
        signer = PythonRSASigner(self._adb_key.public_key, self._adb_key.private_key)
        await self._adb.connect(rsa_keys=[signer])

    async def close(self) -> None:
        await self._adb.close()

    async def reconnect(self) -> None:
        await self.close()
        await self.connect()

    async def update(self) -> None:
        dumpsys_power = await self._send_command(CMD_DUMPSYS_POWER)
        awake = self._parse_awake(dumpsys_power)
        if not awake:
            new_state = DeviceState(
                awake=awake,
                screen_on=False,
                playback_state=STATE_OFF,
            )
        else:
            dumpsys_display = await self._send_command(CMD_DUMPSYS_DISPLAY)
            dumpsys_activity = await self._send_command(CMD_DUMPSYS_ACTIVITY)
            dumpsys_media_session = await self._send_command(CMD_DUMPSYS_MEDIA_SESSION)

            app = self._parse_app(dumpsys_activity)
            if app:
                playback_state = self._parse_playback_state(
                    dumpsys_power, dumpsys_media_session, app
                )
            else:
                playback_state = None

            app_name = APP_NAMES.get(app, app) if app else None

            new_state = DeviceState(
                awake=self._parse_awake(dumpsys_power),
                screen_on=self._parse_screen_on(dumpsys_display),
                app=app_name,
                playback_state=playback_state,
            )

        self._state = new_state

    async def _send_command(
        self,
        command: str,
        retries: int = ADB_MAX_RETRIES,
        retry_interval: float = ADB_RETRY_INTERVAL,
    ) -> str:
        for _ in range(retries):
            if self._timeout_counter >= ADB_MAX_TIMEOUTS:
                await self.reconnect()

            try:
                result = await self._adb.shell(command)
            except TcpTimeoutException:
                self._timeout_counter += 1
                await asyncio.sleep(retry_interval)
                continue

            self._timeout_counter = 0

            if CMD_DUMPSYS_ERROR not in result:
                return result

            await asyncio.sleep(retry_interval)

        raise GoogleTvException(f"Failed to send command {command}")

    def _parse_awake(self, dumpsys_power: str) -> bool | None:
        if re.search(REGEX_AWAKE, dumpsys_power):
            return True
        if re.search(REGEX_ASLEEP, dumpsys_power):
            return False
        return None

    def _parse_screen_on(self, dumpsys_display: str) -> bool | None:
        if re.search(REGEX_SCREEN_ON, dumpsys_display):
            return True
        if re.search(REGEX_SCREEN_OFF, dumpsys_display):
            return False
        return None

    def _parse_app(self, dumpsys_activity: str) -> str | None:
        matches = search_nested(
            (REGEX_ACTIVITY, REGEX_ACTIVITY_RESUMED), dumpsys_activity
        )
        if matches:
            return matches[0].group("app")

        return None

    def _parse_playback_state(
        self, dumpsys_power: str, dumpsys_media_session: str, app: str
    ) -> str | None:
        wl_match = re.search(REGEX_WAKE_LOCK_SIZE, dumpsys_power)
        if not wl_match:
            return None

        ms_matches = search_nested(
            (REGEX_SESSION, app, REGEX_PLAYBACK_STATE), dumpsys_media_session
        )
        if not ms_matches:
            return None

        wake_lock_size = int(wl_match.group("wake_lock_size"))
        media_session_state = int(ms_matches[2].group("state"))

        # ATV Launcher
        if app in [APP_ATV_LAUNCHER, None]:
            return STATE_IDLE

        # Netflix
        elif app == APP_NETFLIX:
            if media_session_state == 2:
                return STATE_PAUSED
            elif media_session_state == 3:
                return STATE_PLAYING
            else:
                return STATE_IDLE

        # NLZIET
        elif app == APP_NLZIET:
            if wake_lock_size == 1:
                return STATE_PAUSED
            elif wake_lock_size == 2:
                return STATE_PLAYING
        # Plex
        elif app == APP_PLEX:
            if media_session_state == 3:
                if wake_lock_size == 1:
                    return STATE_PAUSED
                else:
                    return STATE_PLAYING
            else:
                return STATE_IDLE

        # TVheadend
        elif app == APP_TVHEADEND:
            if wake_lock_size == 5:
                return STATE_PAUSED
            elif wake_lock_size == 6:
                return STATE_PLAYING
            else:
                return STATE_IDLE

        # VLC
        elif app == APP_VLC:
            if media_session_state == 2:
                return STATE_PAUSED
            elif media_session_state == 3:
                return STATE_PLAYING
            else:
                return STATE_IDLE

        # YouTube
        elif app == APP_YOUTUBE:
            if media_session_state == 2:
                return STATE_PAUSED
            elif media_session_state == 3:
                return STATE_PLAYING
            else:
                return STATE_IDLE

        # Get the state from `media_session_state`
        elif media_session_state:
            if media_session_state == 2:
                return STATE_PAUSED
            elif media_session_state == 3:
                return STATE_PLAYING
            else:
                return STATE_IDLE

        # Get the state from `wake_lock_size`
        else:
            if wake_lock_size == 1:
                return STATE_PAUSED
            elif wake_lock_size == 2:
                return STATE_PLAYING
            else:
                return STATE_IDLE

        return None
