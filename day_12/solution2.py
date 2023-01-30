import heapq
from collections import deque


with open('input.txt') as f:
    data = f.read().split('\n')


def print_terrain():
    for line in TERRAIN:
        print(''.join(line))


def find_location(height):
    for y, line in enumerate(TERRAIN):
        for x, char in enumerate(line):
            if char == height:
                return (x, y)


def find_locations(height):
    locations = []
    for y, line in enumerate(TERRAIN):
        for x, char in enumerate(line):
            if char == height:
                locations.append((x, y))
    return locations


########## Breadth First search ##########
def viable_neighbors(loc, max_height_climb):
    x, y = loc
    current_height = TERRAIN[y][x]
    if current_height == 'S': current_height = 'a'
    if current_height == 'E': current_height = 'z'

    neighbors = []
    
    for move in POSSIBLE_MOVES:
        next_x = x + move[0]
        next_y = y + move[1]
        if next_x < 0 or next_y < 0 or next_x >= len(TERRAIN[0]) or next_y >= len(TERRAIN): continue
        next_height = TERRAIN[next_y][next_x]
        if next_height == 'S': next_height = 'a'
        if next_height == 'E': next_height = 'z'

        if ord(next_height) - ord(current_height) <= max_height_climb:
            neighbors.append((next_x, next_y))
    return neighbors


def breadth_first_search(start, end, max_height_climb):
    global bfs_neighbors
    frontier =  deque([start])
    came_from = {start: None}
    
    while frontier:
        current = frontier.popleft()
        if current == end: break

        neighbors = viable_neighbors(current, max_height_climb)
        for neighbor in neighbors:
            if neighbor not in came_from:
                came_from[neighbor] = current
                frontier.append(neighbor)
            if neighbor == end: break

    if current != end: return None
        
    route = [current]
    while route[-1] != start:
        route.append(came_from[current])
        current = came_from[current]
    return list(reversed(route))


########## Dijkstra's search ##########
""" 
This section can give the accepeted answer if the heigh_penalty_mult is 1 and
the heigh_limit is 1 to effectively make an unweighted graph. 
Just wrote this to learn it.
"""
def dijkstra_neighbors(loc, max_height_climb):
    x, y = loc[1]
    current_height = TERRAIN[y][x]
    if current_height == 'S': current_height = 'a'
    if current_height == 'E': current_height = 'z'

    neighbors = []

    for move in POSSIBLE_MOVES:
        next_x = x + move[0]
        next_y = y + move[1]
        if next_x < 0 or next_y < 0 or next_x >= len(TERRAIN[0]) or next_y >= len(TERRAIN): continue
        next_height = TERRAIN[next_y][next_x]
        if next_height == 'S': next_height = 'a'
        if next_height == 'E': next_height = 'z'

        height_diff = ord(next_height) - ord(current_height)
        if height_diff <= max_height_climb:
            cost = 1 if height_diff < 1 else height_diff
            neighbors.append((cost, (next_x, next_y)))
    return neighbors


def dijkstra_search(start, end, max_height_climb):
    global d_neighbors
    frontier    = [(0, start)]
    came_from   = {start: None}
    cost_so_far = {start: 0}

    while frontier:
        current = heapq.heappop(frontier)
        if current[1] == end: break

        neighbors = dijkstra_neighbors(current, max_height_climb)
        for neighbor in neighbors:
            new_cost = cost_so_far[current[1]] + neighbor[0]
            if neighbor[1] not in cost_so_far or new_cost < cost_so_far[neighbor[1]]:
                cost_so_far[neighbor[1]] = new_cost
                came_from[neighbor[1]] = current[1]
                heapq.heappush(frontier, neighbor)
            if neighbor[1] == end: break

    if current[1] != end: return None

    current = current[1]
    route = [current]
    while route[-1] != start:
        route.append(came_from[current])
        current = came_from[current]
    return list(reversed(route))


                



TERRAIN = [list(line) for line in data]
POSSIBLE_MOVES = [(0, 1), (1, 0), (-1, 0), (0, -1)]
max_height_climb = 1
start_coord = find_location('S')
end_coord = find_location('E')

### part 1

shortest_path = breadth_first_search(start_coord, end_coord, max_height_climb)
ans1 = len(shortest_path) -1
print(f"part 1 BFS answer: {ans1}")

shortest_path = dijkstra_search(start_coord, end_coord, max_height_climb)
ans1 = len(shortest_path) -1
print(f"part 1 Dijkstra answer: {ans1}")



### Part 2

# starting_locations = [find_location('S')] + find_locations('a')

# distances = set()
# for start in starting_locations:
#     route = breadth_first_search(start, end_coord, max_height_climb)
#     if route is not None:
#         distances.add(len(route) - 1)

# print(f"part 2 answer: {min(distances)}")

