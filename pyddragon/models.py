class Champion:
    def __init__(self, data: dict):
        self.data = {
            "name": data["name"],  # Aurelion Sol
            "id": data["id"],  # AurelionSol
            "key": data["key"],  # "266"
            "title": data["title"],  # The Star Forger
            "blurb": data["blurb"],  # Aurelion Sol once graced...
            "image": data["image"],  # AurelionSol.png
            "tags": data["tags"],  # ["Mage"]
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


class Item:
    def __init__(self, data: dict):
        self.data = {
            "name": data["name"],  # Perfectly Timed Stopwatch
            "id": data["id"],  # "2423"
            "colloq": data["colloq"],  # ;zhg;zonyas
            "plaintext": data["plaintext"],  # Activate to become...
            "image": data["image"],  # 2423.png
            "gold": data[
                "gold"
            ],  # {"base": 650, "purchasable": False, "total": 650, "sell": 260}
            "tags": data["tags"],  # ["Active"]
            "stats": data["stats"],  # Fake: {"FlatHPPoolMod": 200}
        }

    @property
    def name(self):
        return self.data["name"]

    @property
    def id(self):
        return self.data["id"]

    @property
    def colloq(self):
        return self.data["colloq"]

    @property
    def plaintext(self):
        return self.data["plaintext"]

    @property
    def image(self):
        return self.data["image"]

    @property
    def gold(self):
        return self.data["gold"]

    @property
    def tags(self):
        return self.data["tags"]

    @property
    def stats(self):
        return self.data["stats"]
