import time

start_time = time.time()
def incr_cycle1(x: int, cycle: int, result: int):
    cycle += 1
    if cycle == 20 or (cycle-20) % 40 == 0:
        result += cycle*x
    return cycle, result


def incr_cycle2(x: int, cycle: int, result: str):
    if cycle % 40 == 0:
        result +='\n'
    if cycle-(cycle//40)*40 in [x-1, x, x+1]:
        result += '#'
    else:
        result += '.'
    cycle += 1
    return cycle, result


def run_cycles(incrementer: callable, result):
    x = 1
    cycle = 0
    for line in data:
        cmd = line[:4]
        if cmd == 'addx':
            cycle, result = incrementer(x, cycle, result)
            cycle, result = incrementer(x, cycle, result)
            x += int(line[5:])
        elif cmd == 'noop':
            cycle, result = incrementer(x, cycle, result)
    return result


with open('input.txt') as f:
    data = f.read().splitlines()

print(f"Part 1: {run_cycles(incr_cycle1, 0)}")
print(f"Part 2: {run_cycles(incr_cycle2, '')}")
elapsed = time.time() - start_time
end_time = time.time()
print(f"Time: {round((elapsed)*1000, 4)}ms")
