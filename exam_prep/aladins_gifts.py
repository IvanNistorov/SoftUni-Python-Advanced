from collections import deque
# gemstone = 100 - 199
# porcelain sculpture = 200 - 299
# gold = 300 - 399
# diamond jewellery = 400 - 499
gemstone = 0
porcelain_sculpture = 0
gold = 0
diamond_jewellery = 0

materials_value = [int(x) for x in input().split()]
magic_value = deque([int(x) for x in input().split()])

while materials_value and magic_value:
    material = materials_value.pop()
    magic = magic_value.popleft()

    total = material + magic

    if total < 100:
        if total % 2 == 0:
            material *= 2
            magic *= 3
            total = material + magic
        else:
            total *= 2

    elif total > 499:
        total /= 2

    if 100 <= total <= 499:
        if 100 <= total <= 199:
            gemstone += 1
        elif 200 <= total <= 299:
            porcelain_sculpture += 1
        elif 300 <= total <= 399:
            gold += 1
        elif 400 <= total <= 499:
            diamond_jewellery += 1

if gemstone > 0 and porcelain_sculpture > 0 or gold > 0 and diamond_jewellery > 0:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials_value:
    print(f"Materials left: {', '.join([str(x) for x in materials_value])}")
if magic_value:
    print(f"Magic left: {', '.join([str(x) for x in magic_value])}")

if diamond_jewellery > 0:
    print(f"Diamond Jewellery: {diamond_jewellery}")
if gemstone > 0:
    print(f"Gemstone: {gemstone}")
if gold > 0:
    print(f"Gold: {gold}")
if porcelain_sculpture > 0:
    print(f"Porcelain Sculpture: {porcelain_sculpture}")

