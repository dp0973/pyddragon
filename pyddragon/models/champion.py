from typing import Any


class Champion:
    def __init__(self, data: dict[str, Any]):
        self._data = data

    @property
    def name(self) -> str:
        return self._data["name"]

    @property
    def id(self) -> str:
        return self._data["id"]

    @property
    def key(self) -> str:
        return self._data["key"]

    @property
    def title(self) -> str:
        return self._data["title"]

    @property
    def blurb(self) -> str:
        return self._data["blurb"]

    @property
    def image(self) -> str:
        return self._data["image"]["full"]

    @property
    def tags(self) -> list[str]:
        return self._data["tags"]
