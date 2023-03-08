with open('input.txt') as f:
    lines = f.read().splitlines()

dir_stack = []
dir_sizes = {}

for line in lines:
    if line.startswith("$ ls") or line.startswith("dir"): continue
    if line.startswith("$ cd"):
        if line.split()[-1] == "/":
            dir_stack = ['/']
        elif line.split()[-1] == "..":
            _ = dir_stack.pop()
        else:
            dir_stack.append(dir_stack[-1]+line.split()[-1]+"/")
    else:
        size, file = line.split()
        for d in dir_stack:
            dir_sizes[d] = dir_sizes.setdefault(d, 0) + int(size)

ans1 = sum([size for size in dir_sizes.values() if size < 100000])
print(f"Part 1 answer: {ans1}")

ans2 = sorted([d for d in dir_sizes.values() if d > 30000000 - (70000000 - dir_sizes['/'])])[0]
print(f"Part 2 answer: {ans2}")

        