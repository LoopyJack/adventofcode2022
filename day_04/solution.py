with open('./day_04/input.txt') as f:
    assignments = [tuple((int(elf.split('-')[0]), int(elf.split('-')[1])) for elf in line.split(',')) for line in f.read().splitlines()]

# Part 1
count = 0 # count of contained assignments
for elves in assignments:
    if (elves[0][0] >= elves[1][0] and elves[0][1] <= elves[1][1]) or \
       (elves[1][0] >= elves[0][0] and elves[1][1] <= elves[0][1]):
        count += 1
print(f"Part 1: {count}")

# Part 2
count = 0 # count of overlapping assignments
for elves in assignments:
    if (elves[0][1] >= elves[1][0] and elves[0][0] <= elves[1][1]) or \
       (elves[1][1] >= elves[0][0] and elves[1][0] <= elves[0][1]):
        count += 1
print(f"Part 2: {count}")


        