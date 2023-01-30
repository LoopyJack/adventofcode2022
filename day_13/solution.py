from functools import cmp_to_key
import json

with open('./day_13/input.txt') as f:
    data = f.read().split('\n\n')

pairs = [list(map(json.loads, line.split())) for line in data]


def check_pair(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right: # correct order
            return 1
        elif left > right: # incorrect order
            return -1
        else:
             return None # equal so defer

    elif isinstance(left, list) and isinstance(right, list):
        for i in range(min(len(left), len(right))):
            check = check_pair(left[i], right[i])

            if check is not None: return check

        if len(left) < len(right):
            return 1
        elif len(left) > len(right):
            return -1
        else:
            return None

    elif isinstance(left, int): # right is implied to be list
        return check_pair([left], right)
    elif isinstance(right, int): # left is implied to be list
        return check_pair(left, [right])


check_sum = 0
for i, pair in enumerate(pairs):
    if check_pair(pair[0], pair[1]):
        check_sum += i+1
print(f"part1: {check_sum}")

with open('./day_13/input.txt') as f:
    data = [[[2]],[[6]]] + list(map(json.loads, f.read().replace('\n\n', '\n').splitlines()))

data.sort(key=cmp_to_key(check_pair))
data.reverse()
print(f"part 2: {(data.index([[2]])+1)*(data.index([[6]])+1)}")
