from collections import deque

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


########### Part 2 ###########

# add empty space around the object so that the bfs can travel to all outer surfaces
padding = 3
cube_offset = 1
GRID = [[[ '.' for _ in range(max_z + padding)] for _ in range(max_y + padding)] for _ in range(max_x + padding)]
for cube in cubes:
    GRID[cube[0]+cube_offset][cube[1]+cube_offset][cube[2]+cube_offset] = 'x'


POSSIBLE_MOVES = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

def get_neighbors_and_contacts(loc):
    x, y, z = loc
    neighbors = []
    surface_contacts = 0
    for move in POSSIBLE_MOVES:
        next_x = x + move[0]
        next_y = y + move[1]
        next_z = z + move[2]
        
        if ( 
            next_x < 0 or next_y < 0 or next_z < 0 or 
            next_x >= len(GRID) or next_y >= len(GRID[0]) or next_z >= len(GRID[0][0])
        ): continue
        elif GRID[next_x][next_y][next_z] == 'x':
            surface_contacts += 1
        else:
            neighbors.append((next_x, next_y, next_z))
    return neighbors, surface_contacts


def bfs(start):
    total_surface_contacts = 0
    frontier = deque([start])
    visited = set()

    while frontier:
        current = frontier.popleft()
        neighbors, surface_contacts = get_neighbors_and_contacts(current)
        total_surface_contacts += surface_contacts
        for neighbor in neighbors:
            if neighbor not in visited:
                frontier.append(neighbor)
                visited.add(neighbor)
    return total_surface_contacts

ans = bfs((0,0,0))
print(f'part 2 answer: {ans}')
