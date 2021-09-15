from typing import Any, Optional


class Rune:
    def __init__(self, data: dict[str, Any]):
        self._data = data

    @property
    def name(self) -> str:
        return self._data["name"]

    @property
    def id(self) -> str:
        return self._data["key"]

    @property
    def key(self) -> str:
        return self._data["id"]

    @property
    def icon(self) -> str:
        return self._data["icon"]

    @property
    def short_desc(self) -> Optional[str]:
        return self._data["shortDesc"]

    @property
    def long_desc(self) -> Optional[str]:
        return self._data["longDesc"]
