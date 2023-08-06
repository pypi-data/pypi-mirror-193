import re
from typing import Sequence


def search_nested(
    patterns: Sequence[str], string: str, flags: int = 0
) -> Sequence[re.Match[str]] | None:
    matches = list(re.finditer(patterns[0], string, flags))
    for i, match in enumerate(matches):
        if len(patterns) == 1:
            return (match,)

        start = match.start()
        try:
            end = matches[i + 1].start()
        except IndexError:
            end = len(string)

        nested_match = search_nested(patterns[1:], string[start:end], flags)
        if nested_match:
            return (match, *nested_match)

    return None
