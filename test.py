from pyddragon import ddragon
import asyncio


async def main():
    dd = ddragon.Ddragon()
    aatrox = await dd.get_champion("Aatrox")
    print(aatrox.key)  # 266


asyncio.run(main())
