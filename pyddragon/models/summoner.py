from typing import Any


class Summoner:
    def __init__(self, data: dict[str, Any]) -> None:
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
    def description(self) -> str:
        return self._data["description"]

    @property
    def cooldown(self) -> str:
        return self._data["cooldownBurn"]

    @property
    def modes(self) -> list[str]:
        return self._data["modes"]

    @property
    def range(self) -> str:
        return self._data["rangeBurn"]

    @property
    def image(self) -> str:
        return self._data["image"]["full"]
