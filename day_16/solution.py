from functools import cache
from dataclasses import dataclass
from collections import deque
from itertools import zip_longest

@dataclass(slots=True)
class Valve:
    name: str
    flowrate: int
    neighbors: tuple


valves = {}
shortest_dists = {}

# plain old dicts instead of classes
flows = {}
tunnels = {}


with open('./day_16/example.txt') as f:
        lines = f.read().splitlines()

for line in lines:
    data = line.split()
    name = data[1]
    flowrate = int(data[4].split('=')[1][:-1]) 
    neighbors = [d.strip(', ') for d in data[9:]]
    valves[name] = Valve(name, flowrate, neighbors)
    flows[name] = int(data[4].split('=')[1][:-1]) 
    tunnels[name] = [d.strip(', ') for d in data[9:]]


dists = {}

for valve in flows:
    if valve != 'AA' and not valves[valve]:
        continue
    
    dists[valve] = {
        valve: 0,
        'AA': 0
    }
    visited = {valve}

    queue = deque([(0, valve)])

    while queue:
        distance, position = queue.popleft()
        for neighbor in tunnels[position]:
            if neighbor in visited:
                continue
            visited.add(neighbor)
            if flows[neighbor]:
                dists[valve][neighbor] = distance + 1
            queue.append((distance + 1, neighbor))

    del dists[valve][valve]
    if valve != 'AA':
        del dists[valve]['AA']
    


sequence1 = []
sequence2 = []


# finds shortest distance between two valves
# recursive bfs
# removes destinations where flow is 0
def find_shortest_dists(shortest_dists, start, cur, step_count, check_queue):
    step_count += 1
    for neighbor in valves[cur].neighbors:
        if neighbor != start and neighbor not in shortest_dists:
            shortest_dists[neighbor] = step_count 
            if neighbor not in check_queue:
                check_queue.append(neighbor)
    while check_queue:
            to_check = check_queue.pop(0)
            find_shortest_dists(shortest_dists, start, to_check, shortest_dists[to_check], check_queue)
    return {k:v for k, v in shortest_dists.items() if valves[k].flowrate > 0 and k != start }


# clearer than original function above
# bfs
# removes destinations where flow is 0
def find_shortest_dists2(start, valves):
    check_queue = [start]
    shortest_dists = {start: 0}
    while len(check_queue) > 0:
        cur = check_queue.pop(0)
        for neighbor in valves[cur].neighbors:
            if neighbor not in shortest_dists:
                shortest_dists[neighbor] = shortest_dists[cur] + 1
                check_queue.append(neighbor)
    return {k:v for k, v in shortest_dists.items() if valves[k].flowrate > 0 and k != start }




shortest_dists = {}
for valve in valves:
    if valves[valve].flowrate > 0 or valve == 'AA':
        shortest_dists[valve] = find_shortest_dists({}, valve, valve, 0, [])

shortest_dists2 = {}
for valve in valves:
    if valves[valve].flowrate > 0 or valve == 'AA':
        shortest_dists2[valve] = find_shortest_dists2(valve, valves)

offset = 1
for i in range(len(sequence1)):
    if sequence1[i] != sequence2[i+offset]:
        print('offset')
        offset += 1
    print(sequence1[i] == sequence2[i+offset], sequence1[i], sequence2[i+offset])


for k, v in shortest_dists.items():
    print(f'{k}: {v}')

for k, v in shortest_dists2.items():
    print(f'{k}: {v}')





print(shortest_dists)