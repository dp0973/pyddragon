from typing import Literal, Optional, Union

from aiohttp import ClientSession

from pyddragon.models.champion import Champion
from pyddragon.models.item import Item
from pyddragon.models.rune import Rune
from pyddragon.models.summoner import Summoner
from pyddragon.request import DdragonHttpClient


class Ddragon(DdragonHttpClient):
    def __init__(
        self, lang: str = "en_US", session: Optional[ClientSession] = None
    ) -> None:
        super().__init__(session)
        self.lang = lang
        self.ch_loaded = False
        self.it_loaded = False
        self.ru_loaded = False
        self.su_loaded = False

    async def load_champion(self) -> None:
        self.ch_by_name = {}
        self.ch_by_key = {}
        self.ch_by_id = {}
        ch_props = ["name", "id", "key", "title", "blurb", "image", "tags"]

        chs_json = await self.get_base_json("champion", self.lang)
        for ch in chs_json["data"]:
            ch_json = chs_json["data"][ch]

            data = {}
            for prop in ch_props:
                data[prop] = ch_json[prop]

            ch_data = Champion(data)

            self.ch_by_name[ch_json["name"]] = ch_data
            self.ch_by_id[ch_json["id"]] = ch_data
            self.ch_by_key[int(ch_json["key"])] = ch_data

        self.ch_loaded = True

    async def load_item(self) -> None:
        self.it_by_name = {}
        self.it_by_id = {}
        it_keys = [
            "name",
            "id",
            "colloq",
            "plaintext",
            "image",
            "gold",
            "tags",
            "stats",
            "from",
            "into",
        ]

        its_json = await self.get_base_json("item", self.lang)
        for it in its_json["data"]:
            it_json = its_json["data"][it]

            data = {}
            for prop in it_keys:
                if prop == "id":
                    data[prop] = it
                    continue

                if prop == "from" or prop == "into":
                    data[prop] = it_json.get(prop, [])
                    continue

                data[prop] = it_json[prop]

            it_data = Item(data)

            self.it_by_name[it_json["name"]] = it_data
            self.it_by_id[int(it)] = it_data

        self.it_loaded = True

    async def load_rune(self) -> None:
        self.ru_by_name = {}
        self.ru_by_id = {}
        self.ru_by_key = {}
        ru_keys = ["name", "id", "key", "icon", "shortDesc", "longDesc"]

        rus_json = await self.get_base_json("runesReforged", self.lang)
        for i in range(0, 5):
            field_json = rus_json[i]

            data = {}
            for prop in ru_keys:
                data[prop] = field_json.get(prop, None)

            ru_data = Rune(data)

            self.ru_by_name[field_json["name"]] = ru_data
            self.ru_by_id[field_json["key"]] = ru_data
            self.ru_by_key[str(field_json["id"])] = ru_data

            for slot in field_json["slots"]:
                for ru in slot["runes"]:
                    data = {}
                    for prop in ru_keys:
                        data[prop] = ru[prop]

                    ru_data = Rune(data)

                    self.ru_by_name[ru["name"]] = ru_data
                    self.ru_by_id[ru["key"]] = ru_data
                    self.ru_by_key[int(ru["id"])] = ru_data

        self.ru_loaded = True

    async def load_summoner(self) -> None:
        self.su_by_name = {}
        self.su_by_id = {}
        self.su_by_key = {}
        su_keys = [
            "name",
            "id",
            "key",
            "description",
            "cooldown",
            "modes",
            "range",
            "image",
        ]

        sus_json = await self.get_base_json("summoner", self.lang)
        for su in sus_json["data"]:
            su_json = sus_json["data"][su]

            data = {}
            for prop in su_keys:
                data[prop] = su_json[prop]

            su_data = Summoner(data)

            self.su_by_name[su_json["name"]] = su_data
            self.su_by_id[su_json["id"]] = su_data
            self.su_by_key[int(su_json["key"])] = su_data

        self.su_loaded = True

    async def get_champion(
        self, query: Union[str, int], type: Literal["id", "name"] = "id"
    ) -> Champion:
        if not self.ch_loaded:
            await self.load_champion()

        if isinstance(query, int):
            return self.ch_by_key[query]
        if query.isdigit():
            return self.ch_by_key[int(query)]

        if type == "id":
            return self.ch_by_id[query]

        return self.ch_by_name[query]

    async def get_item(self, query: Union[str, int]) -> Item:
        if not self.it_loaded:
            await self.load_item()

        if isinstance(query, int):
            return self.it_by_id[query]
        if query.isdigit():
            return self.it_by_id[int(query)]

        return self.it_by_name[query]

    async def get_rune(
        self, query: Union[str, int], type: Literal["id", "name"] = "id"
    ) -> Rune:
        if not self.ru_loaded:
            await self.load_rune()

        if isinstance(query, int):
            return self.ru_by_key[query]
        if query.isdigit():
            return self.ru_by_key[int(query)]

        if type == "id":
            return self.ru_by_id[query]

        return self.ru_by_name[query]

    async def get_summoner(
        self, query: Union[str, int], type: Literal["id", "name"] = "id"
    ) -> Summoner:
        if not self.su_loaded:
            await self.load_summoner()

        if isinstance(query, int):
            return self.su_by_key[query]
        if query.isdigit():
            return self.su_by_key[int(query)]

        if type == "id":
            return self.su_by_id[query]

        return self.su_by_name[query]
