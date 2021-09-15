class Champion:
    def __init__(self, data: dict):
        self._data = data

    @property
    def name(self):
        return self._data["name"]

    @property
    def id(self):
        return self._data["id"]

    @property
    def key(self):
        return self._data["key"]

    @property
    def title(self):
        return self._data["title"]

    @property
    def blurb(self):
        return self._data["blurb"]

    @property
    def image(self):
        return self._data["image"]

    @property
    def tags(self):
        return self._data["tags"]