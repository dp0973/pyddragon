from typing import Any


class Item:
    def __init__(self, data: dict[str, Any]):
        self._data = data

    @property
    def name(self) -> str:
        return self._data["name"]

    @property
    def id(self) -> str:
        return self._data["id"]

    @property
    def colloq(self) -> str:
        return self._data["colloq"]

    @property
    def plaintext(self) -> str:
        return self._data["plaintext"]

    @property
    def image(self) -> str:
        return self._data["image"]["full"]

    @property
    def gold(self) -> dict[str, Any]:
        return self._data["gold"]

    @property
    def tags(self) -> list[str]:
        return self._data["tags"]

    @property
    def stats(self) -> dict[str, int]:
        return self._data["stats"]

    @property
    def item_from(self) -> list[str]:
        return self._data["from"]

    @property
    def item_into(self) -> list[str]:
        return self._data["into"]
