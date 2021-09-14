from typing import Optional, Union

from pyddragon.models import Champion
from pyddragon.request import DdragonHttpClient


class Ddragon:
    def __init__(self, lang: Optional[str] = "en_US") -> None:
        self.http = DdragonHttpClient()
        self.lang = lang
        self.loaded = False

    def set_ch_data(self, ch_data: dict[str, str]) -> dict[str, str]:
        data = {}
        for key in self.ch_keys:
            data[key] = ch_data[key]

        return Champion(data)

    async def load_champion(self) -> None:
        self.ch_by_name = {}
        self.ch_by_key = {}
        self.ch_by_id = {}
        self.ch_keys = ["name", "id", "key", "title", "blurb", "image", "tags"]

        chs_json = await self.http.get_base_json("champion", self.lang)
        for ch in chs_json["data"]:
            ch_json = chs_json["data"][ch]
            ch_data = self.set_ch_data(ch_json)

            self.ch_by_name[ch_json["name"]] = ch_data
            self.ch_by_id[ch_json["id"]] = ch_data
            self.ch_by_key[ch_json["key"]] = ch_data

    async def load_all(self) -> None:
        await self.load_champion()
        # await self.load_item()
        # await self.load_summoner()
        # await self.load_rune()

        self.loaded = True

    async def get_champion(self, query: Union[str, int], type: Optional[str] = "id"):
        if not self.loaded:
            await self.load_all()

        if isinstance(query, int):
            return self.ch_by_key[query]
        if query.isdigit():
            return self.ch_by_key[int(query)]

        if type == "id":
            return self.ch_by_id[query]

        return self.ch_by_name[query]
