# pyddragon
<img src="https://img.shields.io/badge/python-v3.9.4-blue"/> [![PyPi version](https://badgen.net/pypi/v/pyddragon/)](https://pypi.com/project/pyddragon) [![PyPi license](https://badgen.net/pypi/license/pyddragon/)](https://pypi.com/project/pyddragon/)  
Python wrapper library providing LoL ddragon data asynchronously

## Features

- Asynchronous
- Supports various search types in a method
- Returns class to get details easily

## Installation

```
pip install pyddragon
```

## Contact & Suggestion

**Just open a pull request or issue freely!**

## Example Code

```py
import asyncio

from pyddragon.ddragon import Ddragon


async def main():
    async with Ddragon() as dd:
        ch_by_name = await dd.get_champion("Aurelion Sol", "name")
        ch_by_id = await dd.get_champion("AurelionSol")
        ch_by_key = await dd.get_champion(136) # "136" is available

        print(f"{ch_by_name.name} - {ch_by_name.id} - {ch_by_name.key}")
        print(f"{ch_by_id.name} - {ch_by_id.id} - {ch_by_id.key}")
        print(f"{ch_by_key.name} - {ch_by_key.id} - {ch_by_key.key}")
        print(f"\n{ch_by_name.blurb}\n")

        it_by_name = await dd.get_item("Sorcerer's Shoes")
        it_by_id = await dd.get_item(3020)

        print(f"{it_by_name.name} - {it_by_name.id}")
        print(f"{it_by_id.name} - {it_by_id.id}")
        print(f"\n{it_by_name.plaintext}\n")

        ru_by_name = await dd.get_rune("Prototype: Omnistone", "name")
        ru_by_id = await dd.get_rune("MasterKey")
        ru_by_key = await dd.get_rune(8358)

        print(f"{ru_by_name.name} - {ru_by_name.id} - {ru_by_name.key}")
        print(f"{ru_by_id.name} - {ru_by_id.id} - {ru_by_id.key}")
        print(f"{ru_by_key.name} - {ru_by_key.id} - {ru_by_key.key}")
        print(f"\n{ru_by_name.short_desc}\n")

        su_by_name = await dd.get_summoner("Barrier", "name")
        su_by_id = await dd.get_summoner("SummonerBarrier")
        su_by_key = await dd.get_summoner(21)

        print(f"{su_by_name.name} - {su_by_name.id} - {su_by_name.key}")
        print(f"{su_by_id.name} - {su_by_id.id} - {su_by_id.key}")
        print(f"{su_by_key.name} - {su_by_key.id} - {su_by_key.key}")
        print(f"\n{su_by_name.image}\n")


asyncio.run(main())
```

Output:
```
Aurelion Sol - AurelionSol - 136
Aurelion Sol - AurelionSol - 136
Aurelion Sol - AurelionSol - 136

Aurelion Sol once graced the vast emptiness of the cosmos with celestial wonders of his own devising. Now, he is forced to wield his awesome power at the behest of a space-faring empire that tricked him into servitude. Desiring a return to his...

Sorcerer's Shoes - 3020
Sorcerer's Shoes - 3020

Enhances Movement Speed and magic damage

Prototype: Omnistone - MasterKey - 8358
Prototype: Omnistone - MasterKey - 8358
Prototype: Omnistone - MasterKey - 8358

Periodically grants a single use of another random keystone.

Barrier - SummonerBarrier - 21
Barrier - SummonerBarrier - 21
Barrier - SummonerBarrier - 21

SummonerBarrier.png
```
