from collections import deque

X = 0
Y = 1
MIN = 2
states = []

def parse_input(file):
    global states
    walls = { 'top': 0, 'left': 0 }
    terrain, blizzards = [], []
    with open(file) as f:
        lines = f.read().splitlines()
        entrance = (lines[0].index('.'), 0)
        exit = (lines[-1].index('.'), len(lines)-1)
        for y, line in enumerate(lines):
            row = [0] * len(line)
            for x, char in enumerate(line):
                if char in ['>', 'v', '<', '^']:
                    blizzards.append([x, y, char])
                    row[x] += 1
            terrain.append(row)
    states.append({'terrain': terrain, 'blizzards': blizzards})
    walls['bottom'] = len(terrain) - 1        
    walls['right' ] = len(terrain[0]) - 1
    return walls, entrance, exit


def draw_terrain(loc, state, entrance):
    terrain = state['terrain']
    blizzards = state['blizzards']
    pic = [['#']*len(terrain[0])]
    pic[0][entrance[X]] = '.'
    for y, row in enumerate(terrain[1:-1]):
        pic_row = ['#']
        for x, col in enumerate(row[1:-1]):
            if col > 1: 
                pic_row.append(str(col))
            elif col == 1:
                for b in blizzards:
                    if b[0]-1 == x and b[1]-1 == y:
                        pic_row.append(b[2])
                        break
            else: 
                pic_row.append('.')
        pic_row.append('#')
        pic.append(pic_row)
    pic.append(['#']*len(terrain[-1]))
    pic[-1][exit[X]] = '.'
    pic[loc[Y]][loc[X]] = 'E'
    for r in pic:
        print(''.join(r))
    print()


def increment_state(state, walls):
    terrain = [row[:] for row in state['terrain']]
    blizzards = [bliz[:] for bliz in state['blizzards']]
    
    for b in blizzards:
        terrain[b[1]][b[0]] -= 1
        if b[2] == '>':
            b[0] += 1
            if b[0] == walls['right']: 
                b[0] = 1    
        elif b[2] == 'v':
            b[1] += 1
            if b[1] == walls['bottom']: 
                b[1] = 1
        elif b[2] == '<':
            b[0] -= 1
            if b[0] == walls['left']: 
                b[0] = walls['right'] - 1
        elif b[2] == '^':
            b[1] -= 1
            if b[1] == walls['top']: 
                b[1] = walls['bottom'] - 1
        terrain[b[1]][b[0]] += 1
    return {'terrain': terrain, 'blizzards': blizzards}


def viable_neighbors(loc, end, walls,):
    global states
    if len(states) == loc[MIN]+1:
        state = increment_state(states[loc[MIN]], walls)
        states.append(state)
    else:
        state = states[loc[MIN]+1]
    neighbors = []
    terrain = state['terrain']
    # right
    if ((loc[Y] > 0 and loc[Y] < len(terrain)-1) # can't move horizontal at entrance/exit
        and (loc[X] < len(terrain[loc[Y]]) - 2 and terrain[loc[Y]][loc[X]+1] == 0)):
        neighbors.append((loc[X]+1, loc[Y], loc[MIN]+1))
    # down
    if ((loc[X] == end[X] and loc[Y]+1 == end[Y]) # exit can be in bottom wall
        or (loc[Y] < len(terrain) - 2 and terrain[loc[Y]+1][loc[X]] == 0)):
        neighbors.append((loc[X], loc[Y]+1, loc[MIN]+1))
    # left
    if ((loc[Y] > 0 and loc[Y] < len(terrain)-1) # can't move horizontal at entrance/exit
        and (loc[X] > 1 and terrain[loc[Y]][loc[X]-1] == 0)):
        neighbors.append((loc[X]-1, loc[Y], loc[MIN]+1))
    # up
    if ((loc[X] == end[X] and loc[Y]-1 == end[Y]) # exit can be in top wall
       or (loc[Y] > 1 and terrain[loc[Y]-1][loc[X]] == 0)):
        neighbors.append((loc[X], loc[Y]-1, loc[MIN]+1))
    # wait
    if terrain[loc[Y]][loc[X]] == 0:
        neighbors.append((loc[X], loc[Y], loc[MIN]+1))
    return neighbors


def find_path(start, end, walls):
    frontier = deque([start])
    came_from = {start: None}

    while frontier:
        loc = frontier.popleft()
        if loc[X] == end[X] and loc[Y] == end[Y]: break

        neighbors = viable_neighbors(loc, end, walls)

        for neighbor in neighbors:
            if neighbor not in came_from:
                came_from[neighbor] = loc
                frontier.append(neighbor)
            if neighbor[X] == end[X] and neighbor[Y] == end[Y]: break

    route = [loc]
    while route[-1] != start:
        route.append(came_from[loc])
        loc = came_from[loc]

    route = list(reversed(route))
    return len(route) -1


walls, entrance, exit = parse_input('input.txt')
start = (entrance[X], entrance[Y], 0)
ans1 = find_path(start, exit, walls)
print(f'part 1 answer: {ans1}')

##### Part 2
ans2 = ans1
ans2 += find_path((exit[X], exit[Y], ans2), entrance, walls) # back to start
ans2 += find_path((entrance[X], entrance[Y], ans2), exit, walls) # back to end again
print(f'part 2 answer: {ans2}')
