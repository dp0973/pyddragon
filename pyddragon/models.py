class Champion:
    def __init__(self, data: dict):
        self.data = {
            "name": data["name"],  # Aurelion Sol
            "id": data["id"],  # AurelionSol
            "key": data["key"],  # 266
            "title": data["title"],  # The Star Forger
            "blurb": data["blurb"],  # Aurelion Sol once graced...
            "image": data["image"],  # AurelionSol.png
            "tags": data["tags"],  # [Mage]
        }

    @property
    def name(self):
        return self.data["name"]

    @property
    def id(self):
        return self.data["id"]

    @property
    def key(self):
        return self.data["key"]

    @property
    def title(self):
        return self.data["title"]

    @property
    def blurb(self):
        return self.data["blurb"]

    @property
    def image(self):
        return self.data["image"]

    @property
    def tags(self):
        return self.data["tags"]
