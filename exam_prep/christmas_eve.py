from collections import deque

elves = deque([int(x) for x in input().split()])
boxes = [int(x) for x in input().split()]

gifts = 0
elves_counter = 0
total_used_energy = 0

while elves and boxes:

    elf_energy = elves.popleft()
    material_box = boxes.pop()

    if elf_energy < 5:
        boxes.append(material_box)
        continue

    elves_counter += 1
    if elves_counter % 3 == 0:
        current_material_box = material_box * 2
        if elf_energy < current_material_box:
            elf_energy *= 2
            elves.append(elf_energy)
            boxes.append(material_box)
        else:
            used_energy = abs(current_material_box - elf_energy)
            if current_material_box == elf_energy:
                total_used_energy += elf_energy
            else:
                if elves_counter % 5 == 0:
                    total_used_energy += elf_energy - used_energy
                    elf_energy -= current_material_box
                    elves.append(elf_energy)
                    continue
                total_used_energy += elf_energy - used_energy
            elf_energy -= current_material_box
            elf_energy += 1
            gifts += 2
            elves.append(elf_energy)

    elif elf_energy < material_box:
        elf_energy *= 2
        elves.append(elf_energy)
        boxes.append(material_box)

    elif elf_energy > material_box:
        used_energy = abs(material_box - elf_energy)
        if material_box == elf_energy:
            total_used_energy += elf_energy
        else:
            if elves_counter % 5 == 0:
                total_used_energy += elf_energy - used_energy
                elf_energy -= material_box
                elves.append(elf_energy)
                continue
            total_used_energy += elf_energy - used_energy
        elf_energy -= material_box
        elf_energy += 1
        gifts += 1
        elves.append(elf_energy)

print(f"Toys: {gifts}")
print(f"Energy: {total_used_energy}")
if elves:
    print(f"Elves left: {', '.join([str(x) for x in elves])}")
if boxes:
    print(f"Boxes left: {', '.join([str(x) for x in boxes])}")
