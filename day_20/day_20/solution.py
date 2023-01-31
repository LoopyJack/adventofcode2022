from collections import deque

with open('input.txt') as f:
    data = f.read().splitlines()

def mix(data: list, decryption_key: int, iterations: int = 1) -> deque:
    values = [int(d)*decryption_key for d in data]
    locations = deque([i for i in range(len(values))])
    for _ in range(iterations):
        for i, v in enumerate(values):
            idx = locations.index(i)
            locations.rotate(-idx)
            to_move = locations.popleft()
            locations.rotate(-v)
            locations.append(to_move)
            locations.rotate(v)
            if v >= 0 : locations.rotate(1)
            if v + idx > len(locations)-1: locations.rotate(1)
        locations.rotate(idx)
    ret = deque([values[l] for l in locations])
    ret.rotate(-ret.index(0))
    return ret

mixed = mix(data, 1, 1)

n1 = mixed[1000 % len(mixed)]
n2 = mixed[2000 % len(mixed)]
n3 = mixed[3000 % len(mixed)]
 
print(f"part 1 answer: {n1+n2+n3}")

######### Part 2 ######### 

decryption_key = 811589153
mixed10 = mix(data, decryption_key, 10)

n1 = mixed10[1000 % len(mixed10)]
n2 = mixed10[2000 % len(mixed10)]
n3 = mixed10[3000 % len(mixed10)]

print(f"part 2 answer: {n1+n2+n3}")