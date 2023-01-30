from itertools import chain, combinations


def get_input():
    with open("./day_16/example.txt") as input_txt:
        input = input_txt.read().splitlines()
    return input


valveset, paths, valves = [], {}, {}


def find_tunnel(position, time, total, minimum, maximum):
    if time <= 0 or len(minimum) == len(valveset):
        if total > maximum[0]:
            maximum[0] = total
    else:
        for calculation in valveset - minimum:
            distance = paths[position][calculation]
            distance_time = time - distance - 1
            distance_total = total
            distance_total += max(0, distance_time * valves[calculation])
            minimum.add(calculation)
            find_tunnel(calculation, distance_time, distance_total, minimum, maximum)
            minimum.remove(calculation)
    return


def part_1(input):
    global valveset, paths, valves
    tunnels = {}

    for iteration, line in enumerate(input):
        parse = line.split()
        flow_rate = int(parse[4][5:-1])
        directions = [direction.rstrip(',') for direction in parse[9:]]
        tunnels[parse[1]] = directions
        if flow_rate > 0:
            valves[parse[1]] = flow_rate
    valveset = set(valves.keys())
    for direction in tunnels.keys():
        distance, list = {direction: 0}, [direction]
        while list:
            first = list[0]
            list = list[1:]
            d = distance[first] + 1
            for tunnel in tunnels[first]:
                if tunnel in distance:
                    assert distance[tunnel] <= d
                else:
                    distance[tunnel] = d
                    list.append(tunnel)
        paths[direction] = distance
    match = [0]
    find_tunnel('AA', 30, 0, set(), match)
    return match[0]


def part_2(input):
    global valveset
    result = 0
    split_set = list(valveset)
    splits = list(chain.from_iterable(combinations(split_set, range) for range in range(len(split_set) + 1)))
    for iteration, split in enumerate(splits):
        split = set(split)
        split_set = valveset - split
        first, second = [0], [0]
        find_tunnel('AA', 26, 0, split, first)
        find_tunnel('AA', 26, 0, split_set, second)
        total = first[0] + second[0]
        if total > result:
            result = total
    return result


if __name__ == "__main__":
    input = get_input()

    part_1 = part_1(input)
    print(f"Puzzle Part 1: {part_1}")

    part_2 = part_2(input)
    print(f"Puzzle Part 2: {part_2}")