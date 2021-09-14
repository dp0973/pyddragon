from typing import Literal, Optional, Union

from pyddragon.models import Champion, Item
from pyddragon.request import DdragonHttpClient


class Ddragon:
    def __init__(self, lang: Optional[str] = "en_US") -> None:
        self.request = DdragonHttpClient()
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

        chs_json = await self.request.get_base_json("champion", self.lang)
        for ch in chs_json["data"]:
            ch_json = chs_json["data"][ch]

            data = {}
            for prop in ch_props:
                if prop == "image":
                    data[prop] = ch_json[prop]["full"]
                    continue

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
        ]

        its_json = await self.request.get_base_json("item", self.lang)
        for it in its_json["data"]:
            it_json = its_json["data"][it]

            data = {}
            for prop in it_keys:
                if prop == "id":
                    data[prop] = it
                    continue

                elif prop == "image":
                    data[prop] = it_json[prop]["full"]
                    continue

                data[prop] = it_json[prop]

            it_data = Item(data)

            self.it_by_name[it_json["name"]] = it_data
            self.it_by_id[int(it)] = it_data

        self.it_loaded = True

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
