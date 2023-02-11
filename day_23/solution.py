from collections import deque

def alone(elf, elves):
    if (elf[0]+1, elf[1]+0) in elves: return False
    if (elf[0]+1, elf[1]+1) in elves: return False
    if (elf[0]+0, elf[1]+1) in elves: return False
    if (elf[0]-1, elf[1]+1) in elves: return False
    if (elf[0]-1, elf[1]+0) in elves: return False
    if (elf[0]-1, elf[1]-1) in elves: return False
    if (elf[0]+0, elf[1]-1) in elves: return False
    if (elf[0]+1, elf[1]-1) in elves: return False
    return True

def check_north(elf, elves):
    if (elf[0]-1, elf[1]-1) in elves: return False 
    if (elf[0]+0, elf[1]-1) in elves: return False
    if (elf[0]+1, elf[1]-1) in elves: return False
    return True
def check_south(elf, elves):
    if (elf[0]-1, elf[1]+1) in elves: return False 
    if (elf[0]+0, elf[1]+1) in elves: return False
    if (elf[0]+1, elf[1]+1) in elves: return False
    return True
def check_east(elf, elves):
    if (elf[0]+1, elf[1]-1) in elves: return False 
    if (elf[0]+1, elf[1]+0) in elves: return False
    if (elf[0]+1, elf[1]+1) in elves: return False
    return True
def check_west(elf, elves):
    if (elf[0]-1, elf[1]-1) in elves: return False 
    if (elf[0]-1, elf[1]+0) in elves: return False
    if (elf[0]-1, elf[1]+1) in elves: return False
    return True

elves = {}
directions = deque(['N', 'S', 'W', 'E'])
step = {
    'N': (0, -1), 
    'S': (0, 1),
    'E': (1, 0),
    'W': (-1, 0)
}
can_move = {
    'N': check_north, 
    'S': check_south,
    'E': check_east,
    'W': check_west
}

min_x = None
min_y = None
max_x = None
max_y = None

with open('input.txt') as f:
    lines = f.read().splitlines()
    for y, row in enumerate(lines):
        for x, char in enumerate(list(row)):
            if char == '#':
                elves[(x, y)] = None
                if min_x is None or x < min_x: min_x = x
                if min_y is None or y < min_y: min_y = y
                if max_x is None or x > max_x: max_x = x
                if max_y is None or y > max_y: max_y = y

rounds = 10
rnd = 0
proposals = 1
while proposals:
    proposals = {}
    for elf in elves:
        if not alone(elf, elves):
            for direction in directions:
                if can_move[direction](elf, elves):
                    proposal = (elf[0]+step[direction][0], elf[1]+step[direction][1])
                    if proposal in proposals:
                        proposals[proposal] = None
                    else:
                        proposals[proposal] = elf
                    break
    to_remove = []
    for proposal, elf in proposals.items():
        if elf is None: continue
        elves[proposal] = None
        to_remove.append(elf)
        if proposal[0] < min_x: min_x = proposal[0]
        if proposal[1] < min_y: min_y = proposal[1]
        if proposal[0] > max_x: max_x = proposal[0]
        if proposal[1] > max_y: max_y = proposal[1]
    for r in to_remove: del elves[r]
    directions.rotate(-1)                
    rnd += 1

    if rnd <= rounds:
        ans1 = ((max_x - min_x)+1) * ((max_y - min_y)+1) - len(elves)

print(f"part 1 answer: {ans1}")
print(f"part 2 answer: {rnd}")

