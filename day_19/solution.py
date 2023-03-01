from collections import deque
from time import time
resources = ['ore', 'clay', 'obsidian', 'geode']
ORE = 0
CLAY = 1
OBSIDIAN = 2
GEODE = 3
TIME = 0
RBTS = 1
AMNT = 2

def timer_func(func):
    # This function shows the execution time of
    # the function object passed
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function {func.__name__!r} executed in {(t2 - t1):.4f}s')
        return result

    return wrap_func


def parse_robot_costs(robots: str) -> tuple:
    robots = robots.split('.')[:-1]
    robots_costs = []
    for r in robots:
        robot_cost = []
        costs = [r.split() for r in r.split('costs')[1].split('and')]
        costs = {cost[1]: int(cost[0]) for cost in costs}
        for resource in resources:
            if resource in costs: 
                robot_cost.append(costs[resource])
            else:
                robot_cost.append(0)
        robots_costs.append(tuple(robot_cost))
    return tuple(robots_costs)


def parse_input(file) -> list:
    with open(file) as f:
        rows = f.read().splitlines()
        blueprints = []
        for row in rows:
            idnum, robots = row.split(':')
            blueprint = {
                'id': int(idnum.split()[1]),
                'robot_costs': parse_robot_costs(robots),
                'max_geodes': 0,
                'end_nodes': 0
            }
            # blueprints[int(idnum.split()[1])] = blueprint
            blueprints.append(blueprint)
    return blueprints


def can_afford_robot(res_idx, costs, state: tuple) -> bool:
    for res, cost in enumerate(costs[res_idx]):
        if cost > state[AMNT][res]:
            return False
    return True


def buy_robot(res_idx, costs, state: tuple) -> tuple:
    new_amounts = list(state[AMNT])
    for res, cost in enumerate(costs[res_idx]):
        new_amounts[res] -= cost
    return (state[TIME], state[RBTS], tuple(new_amounts))
        

def add_robot(res_idx, state: tuple) -> tuple:
    new_robot_count = list(state[RBTS])
    new_robot_count[res_idx] += 1
    return (state[TIME], tuple(new_robot_count), state[AMNT])


def collect_resources(state: tuple) -> tuple:
    new_amounts = list(state[AMNT])
    for i, res in enumerate(state[RBTS]):
        new_amounts[i] += res
    return (state[TIME], state[RBTS], tuple(new_amounts))


def find_max_costs(robot_costs):
    max_costs = [0 for _ in resources]
    for robot in robot_costs:
        for i, res in enumerate(robot):
            if res > max_costs[i]: max_costs[i] = res
    max_costs[-1] = 99999999 # no (realistic) upper bound for geode
    return tuple(max_costs)


@timer_func
def dfs(blueprint, time_limit):
    start_state = (0, (1,0,0,0), (0,0,0,0))
    robot_costs = blueprint['robot_costs']
    max_costs = find_max_costs(robot_costs)
    frontier = deque([start_state])
    visited = set()

    while frontier:
        cur_state = frontier.pop()
        if cur_state[TIME] == time_limit:
            blueprint['end_nodes'] += 1
            if cur_state[AMNT][GEODE] > blueprint['max_geodes']:
                blueprint['max_geodes'] = cur_state[AMNT][GEODE]
                blueprint['state'] = cur_state
            continue

        minutes_left = time_limit - cur_state[TIME] + 1 # add 1 to include current minute
        max_potential_geodes = (minutes_left*(minutes_left+1))/2 + (cur_state[AMNT][GEODE] * minutes_left)
        # max_potential_geodes = cur_state[AMNT][GEODE] + (cur_state[RBTS][GEODE]+1) * minutes_left
        if max_potential_geodes <= blueprint['max_geodes']: continue

        possible_next_states = []

        # no buying
        next_state = (cur_state[TIME]+1, cur_state[RBTS], cur_state[AMNT])
        next_state = collect_resources(next_state)
        possible_next_states.append(next_state)

        for i, r in enumerate(resources):
            if minutes_left > 1 or r == 'geode':
                # don't buy robots
                if cur_state[RBTS][OBSIDIAN] and r == 'ore': continue 
                if cur_state[RBTS][GEODE] and r in ['ore', 'clay']: continue

                if can_afford_robot(i, robot_costs, cur_state) and cur_state[RBTS][i] < max_costs[i]:
                    next_state = (cur_state[TIME]+1, cur_state[RBTS], cur_state[AMNT])
                    next_state = buy_robot(i, robot_costs, next_state)
                    next_state = collect_resources(next_state)
                    next_state = add_robot(i, next_state)
                    if r == 'geode':
                        possible_next_states = [next_state]
                    else:
                        possible_next_states.append(next_state)
        for pns in possible_next_states:
            if pns not in visited:
                visited.add(pns)
                frontier.append(pns)
    return blueprint


blueprints = parse_input('input.txt')
res = []
for bp in blueprints:
    res.append(dfs(bp, 24))
ans1 = print(f"part 1 answer: {sum([bp['id']*bp['max_geodes'] for bp in res])}")

res2 = []
ans2 = 1
for bp in blueprints[:3]:
    res2.append(dfs(bp, 32))
    ans2 *= res2[-1]['max_geodes']
print(f"part 2 answer: {ans2}")





res_old = [{'end_nodes': 1558412,
  'id': 1,
  'max_geodes': 6,
  'robot_costs': ((4, 0, 0, 0), (4, 0, 0, 0), (4, 17, 0, 0), (4, 0, 20, 0)),
  'state': (32, (4, 11, 8, 2), (8, 31, 17, 6))},
 {'end_nodes': 499180,
  'id': 2,
  'max_geodes': 44,
  'robot_costs': ((3, 0, 0, 0), (3, 0, 0, 0), (2, 12, 0, 0), (2, 0, 10, 0)),
  'state': (32, (3, 8, 9, 8), (20, 54, 16, 44))},
 {'end_nodes': 1030432,
  'id': 3,
  'max_geodes': 12,
  'robot_costs': ((3, 0, 0, 0), (3, 0, 0, 0), (2, 20, 0, 0), (3, 0, 18, 0)),
  'state': (32, (3, 12, 9, 3), (15, 33, 21, 12))},
 {'end_nodes': 353256,
  'id': 4,
  'max_geodes': 0,
  'robot_costs': ((3, 0, 0, 0), (3, 0, 0, 0), (3, 19, 0, 0), (3, 0, 17, 0))},
 {'end_nodes': 328465,
  'id': 5,
  'max_geodes': 0,
  'robot_costs': ((3, 0, 0, 0), (4, 0, 0, 0), (4, 18, 0, 0), (3, 0, 13, 0))},
 {'end_nodes': 5752,
  'id': 6,
  'max_geodes': 5,
  'robot_costs': ((2, 0, 0, 0), (4, 0, 0, 0), (2, 16, 0, 0), (2, 0, 9, 0)),
  'state': (24, (4, 10, 6, 2), (20, 23, 11, 5))},
 {'end_nodes': 562602,
  'id': 7,
  'max_geodes': 0,
  'robot_costs': ((4, 0, 0, 0), (3, 0, 0, 0), (3, 14, 0, 0), (4, 0, 17, 0))},
 {'end_nodes': 319852,
  'id': 8,
  'max_geodes': 2,
  'robot_costs': ((3, 0, 0, 0), (4, 0, 0, 0), (4, 18, 0, 0), (3, 0, 8, 0)),
  'state': (24, (4, 10, 5, 1), (5, 11, 10, 2))},
 {'end_nodes': 433063,
  'id': 9,
  'max_geodes': 1,
  'robot_costs': ((4, 0, 0, 0), (4, 0, 0, 0), (2, 9, 0, 0), (3, 0, 15, 0)),
  'state': (24, (1, 3, 4, 1), (1, 7, 7, 1))},
 {'end_nodes': 214966,
  'id': 10,
  'max_geodes': 0,
  'robot_costs': ((4, 0, 0, 0), (4, 0, 0, 0), (2, 15, 0, 0), (3, 0, 16, 0))},
 {'end_nodes': 584845,
  'id': 11,
  'max_geodes': 2,
  'robot_costs': ((2, 0, 0, 0), (4, 0, 0, 0), (3, 19, 0, 0), (4, 0, 13, 0)),
  'state': (24, (4, 11, 6, 1), (10, 11, 13, 2))},
 {'end_nodes': 314206,
  'id': 12,
  'max_geodes': 3,
  'robot_costs': ((3, 0, 0, 0), (3, 0, 0, 0), (4, 19, 0, 0), (4, 0, 7, 0)),
  'state': (24, (2, 7, 3, 1), (4, 32, 9, 3))},
 {'end_nodes': 20220,
  'id': 13,
  'max_geodes': 3,
  'robot_costs': ((3, 0, 0, 0), (4, 0, 0, 0), (2, 15, 0, 0), (3, 0, 7, 0)),
  'state': (24, (4, 8, 4, 2), (17, 27, 7, 3))},
 {'end_nodes': 13790,
  'id': 14,
  'max_geodes': 7,
  'robot_costs': ((3, 0, 0, 0), (4, 0, 0, 0), (3, 10, 0, 0), (2, 0, 7, 0)),
  'state': (24, (4, 7, 6, 3), (16, 22, 11, 7))},
 {'end_nodes': 387350,
  'id': 15,
  'max_geodes': 1,
  'robot_costs': ((4, 0, 0, 0), (4, 0, 0, 0), (2, 10, 0, 0), (3, 0, 14, 0)),
  'state': (24, (1, 3, 4, 1), (1, 3, 6, 1))},
 {'end_nodes': 4766,
  'id': 16,
  'max_geodes': 9,
  'robot_costs': ((4, 0, 0, 0), (4, 0, 0, 0), (4, 5, 0, 0), (3, 0, 7, 0)),
  'state': (24, (2, 2, 5, 3), (2, 5, 9, 9))},
 {'end_nodes': 130250,
  'id': 17,
  'max_geodes': 0,
  'robot_costs': ((4, 0, 0, 0), (4, 0, 0, 0), (3, 20, 0, 0), (2, 0, 10, 0))},
 {'end_nodes': 510387,
  'id': 18,
  'max_geodes': 1,
  'robot_costs': ((4, 0, 0, 0), (3, 0, 0, 0), (3, 15, 0, 0), (2, 0, 13, 0)),
  'state': (24, (1, 4, 3, 1), (1, 11, 4, 1))},
 {'end_nodes': 239149,
  'id': 19,
  'max_geodes': 0,
  'robot_costs': ((4, 0, 0, 0), (4, 0, 0, 0), (2, 14, 0, 0), (4, 0, 19, 0))},
 {'end_nodes': 145849,
  'id': 20,
  'max_geodes': 0,
  'robot_costs': ((4, 0, 0, 0), (4, 0, 0, 0), (4, 18, 0, 0), (4, 0, 9, 0))},
 {'end_nodes': 290795,
  'id': 21,
  'max_geodes': 0,
  'robot_costs': ((3, 0, 0, 0), (4, 0, 0, 0), (3, 20, 0, 0), (3, 0, 14, 0))},
 {'end_nodes': 3108,
  'id': 22,
  'max_geodes': 9,
  'robot_costs': ((4, 0, 0, 0), (3, 0, 0, 0), (4, 8, 0, 0), (3, 0, 7, 0)),
  'state': (24, (1, 2, 2, 2), (4, 21, 8, 9))},
 {'end_nodes': 13445,
  'id': 23,
  'max_geodes': 4,
  'robot_costs': ((2, 0, 0, 0), (4, 0, 0, 0), (3, 19, 0, 0), (4, 0, 8, 0)),
  'state': (24, (4, 11, 5, 2), (9, 30, 8, 4))},
 {'end_nodes': 10419,
  'id': 24,
  'max_geodes': 5,
  'robot_costs': ((4, 0, 0, 0), (4, 0, 0, 0), (4, 5, 0, 0), (2, 0, 10, 0)),
  'state': (24, (2, 2, 5, 2), (3, 4, 9, 5))},
 {'end_nodes': 6282,
  'id': 25,
  'max_geodes': 8,
  'robot_costs': ((4, 0, 0, 0), (3, 0, 0, 0), (4, 8, 0, 0), (2, 0, 8, 0)),
  'state': (24, (1, 2, 3, 2), (2, 13, 7, 8))},
 {'end_nodes': 461404,
  'id': 26,
  'max_geodes': 2,
  'robot_costs': ((3, 0, 0, 0), (4, 0, 0, 0), (4, 14, 0, 0), (4, 0, 10, 0)),
  'state': (24, (4, 9, 5, 1), (7, 17, 10, 2))},
 {'end_nodes': 605425,
  'id': 27,
  'max_geodes': 2,
  'robot_costs': ((2, 0, 0, 0), (4, 0, 0, 0), (4, 18, 0, 0), (2, 0, 11, 0)),
  'state': (24, (4, 11, 6, 1), (6, 17, 15, 2))},
 {'end_nodes': 475038,
  'id': 28,
  'max_geodes': 1,
  'robot_costs': ((3, 0, 0, 0), (3, 0, 0, 0), (2, 16, 0, 0), (3, 0, 14, 0)),
  'state': (24, (2, 9, 4, 1), (3, 34, 8, 1))},
 {'end_nodes': 629383,
  'id': 29,
  'max_geodes': 1,
  'robot_costs': ((2, 0, 0, 0), (3, 0, 0, 0), (3, 18, 0, 0), (2, 0, 19, 0)),
  'state': (24, (3, 11, 6, 1), (6, 17, 10, 1))},
 {'end_nodes': 5819,
  'id': 30,
  'max_geodes': 9,
  'robot_costs': ((2, 0, 0, 0), (4, 0, 0, 0), (4, 11, 0, 0), (3, 0, 8, 0)),
  'state': (24, (4, 8, 6, 4), (8, 38, 8, 9))}]


for i, r in enumerate(res):
    print(r['end_nodes'], res_old[i]['end_nodes'])