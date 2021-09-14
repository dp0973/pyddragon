# pyddragon

> Python wrapper library providing LoL ddragon data asynchronously (On dev)

## Example Code

```py
import asyncio

from pyddragon import ddragon


async def main():
    dd = ddragon.Ddragon()

    ch_by_name = await dd.get_champion("Aurelion Sol", "name")
    ch_by_key = await dd.get_champion(136)
    ch_by_id = await dd.get_champion("AurelionSol")

    print(f"{ch_by_name.name} - {ch_by_name.id} - {ch_by_name.key}")
    print(f"{ch_by_key.name} - {ch_by_key.id} - {ch_by_key.key}")
    print(f"{ch_by_id.name} - {ch_by_id.id} - {ch_by_id.key}")
    print(f"\n{ch_by_name.blurb}\n")

    it_by_name = await dd.get_item("Sorcerer's Shoes")
    it_by_id = await dd.get_item(3020)

    print(f"{it_by_name.name} - {it_by_name.id}")
    print(f"{it_by_id.name} - {it_by_id.id}")
    print(f"\n{it_by_name.plaintext}\n")


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
```
