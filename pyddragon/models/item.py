class Item:
    def __init__(self, data: dict):
        self._data = data

    @property
    def name(self):
        return self._data["name"]

    @property
    def id(self) -> str:
        return self._data["id"]

    @property
    def colloq(self):
        return self._data["colloq"]

    @property
    def plaintext(self):
        return self._data["plaintext"]

    @property
    def image(self):
        return self._data["image"]

    @property
    def gold(self):
        return self._data["gold"]

    @property
    def tags(self):
        return self._data["tags"]

    @property
    def stats(self):
        return self._data["stats"]
