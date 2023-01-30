import itertools

max_x, max_y, max_z = [0,0,0]
cubes = []

with open('input.txt') as f:
    lines = f.read().splitlines()
    for l in lines:
        line = l.split(',')
        if int(line[0]) > max_x : max_x = int(line[0])
        if int(line[1]) > max_y : max_y = int(line[1])
        if int(line[2]) > max_z : max_z = int(line[2])
        cubes.append((int(line[0]), int(line[1]), int(line[2])))

contacts = {cube: 0 for cube in cubes}
exposed = {cube: 6 for cube in cubes}

for i, c1 in enumerate(cubes):
    for i2 in range(i+1, len(cubes)):
        c2 = cubes[i2]
        dist = abs(c2[0]-c1[0]) + abs(c2[1]-c1[1]) + abs(c2[2]-c1[2])
        if dist == 1:
            exposed[c1] -= 1
            exposed[c2] -= 1

print(f'part 1 answer: {sum(exposed.values())}')



for cube in cubes:
    grid[cube[0]-1][cube[1]-1][cube[2]-1] = 'x'
grid = [[[ '.' for _ in range(max_z)] for _ in range(max_y)] for _ in range(max_x)]