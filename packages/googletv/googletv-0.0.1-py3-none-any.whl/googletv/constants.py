ADB_MAX_RETRIES = 3
ADB_RETRY_INTERVAL = 0.25
ADB_MAX_TIMEOUTS = 2

CMD_DUMPSYS_DISPLAY = "dumpsys display"
CMD_DUMPSYS_POWER = "dumpsys power"
CMD_DUMPSYS_ACTIVITY = "dumpsys activity ."
CMD_DUMPSYS_MEDIA_SESSION = "dumpsys media_session"

CMD_DUMPSYS_ERROR = "Error dumping service info"

REGEX_AWAKE = r"mWakefulness=Awake|Dreaming"
REGEX_ASLEEP = r"mWakefulness=Asleep"

REGEX_SCREEN_ON = r"mScreenState=ON"
REGEX_SCREEN_OFF = r"mScreenState=OFF"

REGEX_WAKE_LOCK_SIZE = r"Wake Locks: size=(?P<wake_lock_size>\d+)"

REGEX_ACTIVITY = r"ACTIVITY (?P<app>[^ ]+)\/(?P<activity>[^ ]+)"
REGEX_ACTIVITY_RESUMED = r"mResumed=true"

REGEX_SESSION = r"Sessions Stack"
REGEX_PLAYBACK_STATE = r"state=PlaybackState {state=(?P<state>\d)"

# Playback states

STATE_OFF = "off"
STATE_IDLE = "idle"
STATE_PLAYING = "playing"
STATE_PAUSED = "paused"

# Apps
APP_AE_TV = "com.aetn.aetv.watch"
APP_AMAZON_PRIME_VIDEO = "com.amazon.avod.thirdpartyclient"
APP_AMAZON_VIDEO = "com.amazon.avod"
APP_APPLE_TV_PLUS = "com.apple.atve.androidtv.appletv"
APP_ATV_LAUNCHER = "com.google.android.tvlauncher"
APP_BELL_FIBE = "com.quickplay.android.bellmediaplayer"
APP_CBC_GEM = "ca.cbc.android.cbctv"
APP_COMEDY_CENTRAL = "com.vmn.android.comedycentral"
APP_CRAVE = "ca.bellmedia.cravetv"
APP_DAILYMOTION = "com.dailymotion.dailymotion"
APP_DEEZER = "deezer.android.tv"
APP_DISNEY_PLUS = "com.disney.disneyplus"
APP_DISNEY_PLUS_HOTSTAR = "in.startv.hotstar"
APP_DS_PHOTO = "com.synology.dsphoto"
APP_DS_VIDEO = "com.synology.dsvideo"
APP_ES_FILE_EXPLORER = "com.estrongs.android.pop"
APP_FACEBOOK = "com.facebook.katana"
APP_FAWESOME = "com.future.moviesByFawesomeAndroidTV"
APP_FIREFOX = "org.mozilla.tv.firefox"
APP_FOOD_NETWORK_GO = "tv.accedo.foodnetwork"
APP_FRANCE_TV = "fr.francetv.pluzz"
APP_GLOBAL_TV = "com.shawmedia.smglobal"
APP_GOOGLE_CAST = "com.google.android.apps.mediashell"
APP_GOOGLE_TV_LAUNCHER = "com.google.android.apps.tv.launcherx"
APP_HAYSTACK_NEWS = "com.haystack.android"
APP_HBO_GO = "eu.hbogo.androidtv.production"
APP_HBO_GO_2 = "com.HBO"
APP_HOICHOI = "com.viewlift.hoichoi"
APP_HULU = "com.hulu.plus"
APP_HUNGAMA_PLAY = "com.hungama.movies.tv"
APP_IMDB_TV = "com.amazon.imdb.tv.android.app"
APP_IPTV = "ru.iptvremote.android.iptv"
APP_IPTV_SMARTERS_PRO = "com.nst.iptvsmarterstvbox"
APP_JELLYFIN_TV = "org.jellyfin.androidtv"
APP_JIO_CINEMA = "com.jio.media.stb.ondemand"
APP_KODI = "org.xbmc.kodi"
APP_LIVE_CHANNELS = "com.google.android.tv"
APP_MIJN_RADIO = "org.samsonsen.nederlandse.radio.holland.nl"
APP_MOLOTOV = "tv.molotov.app"
APP_MRMC = "tv.mrmc.mrmc"
APP_MRMC_LITE = "tv.mrmc.mrmc.lite"
APP_MX_PLAYER = "com.mxtech.videoplayer.ad"
APP_NETFLIX = "com.netflix.ninja"
APP_NLZIET = "nl.nlziet"
APP_NOS = "nl.nos.app"
APP_NPO = "nl.uitzendinggemist"
APP_OCS = "com.orange.ocsgo"
APP_PLAY_GAMES = "com.google.android.play.games"
APP_PLAY_MUSIC = "com.google.android.music"
APP_PLAY_STORE = "com.android.vending"
APP_PLAY_VIDEOS = "com.google.android.videos"
APP_PLEX = "com.plexapp.android"
APP_PRIME_VIDEO = "com.amazon.amazonvideo.livingroom"
APP_SETTINGS = "com.android.tv.settings"
APP_SMART_YOUTUBE_TV = "com.liskovsoft.videomanager"
APP_SPORT1 = "de.sport1.firetv.video"
APP_SPOTIFY = "com.spotify.tv.android"
APP_STEAM_LINK = "com.valvesoftware.steamlink"
APP_SYFY = "com.amazon.webapps.nbc.syfy"
APP_T2 = "tv.perception.clients.tv.android"
APP_TED = "com.ted.android.tv"
APP_TUNEIN = "tunein.player"
APP_TVHEADEND = "de.cyberdream.dreamepg.tvh.tv.player"
APP_TWITCH = "tv.twitch.android.app"
APP_VEVO = "com.vevo.tv"
APP_VH1 = "com.mtvn.vh1android"
APP_VIMEO = "com.vimeo.android.videoapp"
APP_VLC = "org.videolan.vlc"
APP_VOYO = "com.phonegap.voyo"
APP_VRV = "com.ellation.vrv"
APP_WAIPU_TV = "de.exaring.waipu.firetv.live"
APP_WATCH_TNT = "com.turner.tnt.android.networkapp"
APP_YOUTUBE = "com.google.android.youtube.tv"
APP_YOUTUBE_KIDS = "com.google.android.youtube.tvkids"
APP_YOUTUBE_MUSIC = "com.google.android.youtube.tvmusic"
APP_YOUTUBE_TV = "com.google.android.youtube.tvunplugged"
APP_ZEE5 = "com.graymatrix.did"
APP_ZIGGO_GO_TV = "com.ziggo.tv"
APP_NAMES = {
    APP_AE_TV: "A&E",
    APP_AMAZON_PRIME_VIDEO: "Amazon Prime Video",
    APP_AMAZON_VIDEO: "Amazon Video",
    APP_APPLE_TV_PLUS: "Apple TV+",
    APP_ATV_LAUNCHER: "Android TV Launcher",
    APP_BELL_FIBE: "Bell Fibe",
    APP_CBC_GEM: "CBC Gem",
    APP_COMEDY_CENTRAL: "Comedy Central",
    APP_CRAVE: "Crave",
    APP_DAILYMOTION: "Dailymotion",
    APP_DEEZER: "Deezer",
    APP_DISNEY_PLUS: "Disney+",
    APP_DISNEY_PLUS_HOTSTAR: "Disney+ Hotstar",
    APP_DS_PHOTO: "DS photo",
    APP_DS_VIDEO: "DS video",
    APP_ES_FILE_EXPLORER: "ES File Explorer",
    APP_FACEBOOK: "Facebook Watch",
    APP_FAWESOME: "Fawsome",
    APP_FIREFOX: "Firefox",
    APP_FOOD_NETWORK_GO: "Food Network GO",
    APP_FRANCE_TV: "France TV",
    APP_GLOBAL_TV: "Global TV",
    APP_GOOGLE_CAST: "Google Cast",
    APP_GOOGLE_TV_LAUNCHER: "Google TV Launcher",
    APP_HAYSTACK_NEWS: "Haystack News",
    APP_HBO_GO: "HBO GO",
    APP_HBO_GO_2: "HBO GO (2)",
    APP_HOICHOI: "Hoichoi",
    APP_HULU: "Hulu",
    APP_HUNGAMA_PLAY: "Hungama Play",
    APP_IMDB_TV: "IMDb TV",
    APP_IPTV: "IPTV",
    APP_IPTV_SMARTERS_PRO: "IPTV Smarters Pro",
    APP_JELLYFIN_TV: "Jellyfin",
    APP_JIO_CINEMA: "Jio Cinema",
    APP_KODI: "Kodi",
    APP_LIVE_CHANNELS: "Live Channels",
    APP_MIJN_RADIO: "Mijn Radio",
    APP_MOLOTOV: "Molotov",
    APP_MRMC: "MrMC",
    APP_MRMC_LITE: "MrMC Lite",
    APP_MX_PLAYER: "MX Player",
    APP_NETFLIX: "Netflix",
    APP_NLZIET: "NLZIET",
    APP_NOS: "NOS",
    APP_NPO: "NPO",
    APP_OCS: "OCS",
    APP_PLAY_GAMES: "Play Games",
    APP_PLAY_MUSIC: "Play Music",
    APP_PLAY_STORE: "Play Store",
    APP_PLAY_VIDEOS: "Play Movies & TV",
    APP_PLEX: "Plex",
    APP_PRIME_VIDEO: "Prime Video",
    APP_SETTINGS: "Settings",
    APP_SMART_YOUTUBE_TV: "Smart YouTube TV",
    APP_SPORT1: "Sport 1",
    APP_SPOTIFY: "Spotify",
    APP_STEAM_LINK: "Steam Link",
    APP_SYFY: "Syfy",
    APP_T2: "T-2 TV",
    APP_TED: "TED",
    APP_TUNEIN: "TuneIn Radio",
    APP_TVHEADEND: "DreamPlayer TVHeadend",
    APP_TWITCH: "Twitch",
    APP_VEVO: "Vevo",
    APP_VH1: "VH1",
    APP_VIMEO: "Vimeo",
    APP_VLC: "VLC",
    APP_VOYO: "VOYO",
    APP_VRV: "VRV",
    APP_WAIPU_TV: "Waipu TV",
    APP_WATCH_TNT: "Watch TNT",
    APP_YOUTUBE: "YouTube",
    APP_YOUTUBE_KIDS: "YouTube Kids",
    APP_YOUTUBE_MUSIC: "YouTube Music",
    APP_YOUTUBE_TV: "YouTube TV",
    APP_ZEE5: "ZEE5",
    APP_ZIGGO_GO_TV: "Ziggo GO TV",
}
