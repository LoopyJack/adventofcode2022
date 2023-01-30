
flows = {}
neighbors = {}


with open('./day_16/input.txt') as f:
        lines = f.read().splitlines()

for line in lines:
    data = line.split()
    name = data[1]
    flows[name] = int(data[4].split('=')[1][:-1]) 
    neighbors[name] = [d.strip(', ') for d in data[9:]]




def recursive_dfs(valve, opened, min_left):
    if min_left <= 0:
        return 0
    total_flow = 0
    if valve not in opened:
        valve_total_flow = flows[valve] * (min_left - 1)
        new_opened = opened + (valve,)
        for next_valve in neighbors[valve]:
            if valve_total_flow > 0:  # open current valve and travel to neighbor
                total_flow = max(total_flow, valve_total_flow + recursive_dfs(next_valve, new_opened, min_left - 2))
            else:  # current valve has no flow and travel to neighbor
                total_flow = max(total_flow, recursive_dfs(next_valve, new_opened, min_left - 1))
    return total_flow

print(recursive_dfs('AA', (), 30))