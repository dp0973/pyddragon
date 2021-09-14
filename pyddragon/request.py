from typing import Any, Literal, Optional
from aiohttp import ClientSession
from types import TracebackType


class DdragonHttpClient:
    BASE_URL = "http://ddragon.leagueoflegends.com"

    def __init__(self, session: Optional[ClientSession] = None) -> None:
        self.session = session
        self.version = None

    async def close(self) -> None:
        if self.session:
            await self.session.close()

    async def __aenter__(self) -> "DdragonHttpClient":
        return self

    async def __aexit__(
        self,
        exc_type: Optional[type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None:
        await self.close()

    async def request(
        self,
        method: Literal["GET"],
        endpoint: str,
        return_type: Optional[str] = None,
        **kwargs: Any,
    ) -> Any:
        if not self.session:
            self.session = ClientSession()

        async with self.session.request(
            method, self.BASE_URL + endpoint, **kwargs
        ) as r:
            if return_type == "json":
                return await r.json()
            return await r.text()

    async def get_version(self) -> str:
        if not self.version:
            self.version = await self.request("GET", "/api/versions.json", "json")

        return self.version[0]

    async def get_base_json(
        self, field: Literal["champion", "item", "runesReforged", "summoner"], lang: str
    ):
        return await self.request(
            "GET", f"/cdn/{await self.get_version()}/data/{lang}/{field}.json", "json"
        )
