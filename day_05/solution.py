import time
start_time = time.time()
def create_stacks(txt):
    numStacks = int(txt[-1].replace(' ', '')[-1])
    stacks = [[] for i in range(numStacks)]

    for i in range(len(txt)-1):
        rIdx = numStacks-2-i
        row = txt[rIdx]
        row = [row[c:c+4][1] for c in range(0, len(row), 4)]
        for sIdx, val in enumerate(row):
            if val != ' ':
                stacks[sIdx].append(val)
    return stacks


def get_top_rearrange_stacks(stacks: list[list[str]], method: callable):
    for line in procedure:
        _, num, _, from_stack, _, to_stack = line.split()
        method(stacks, int(num), int(from_stack), int(to_stack))
    return ''.join([stack[-1] for stack in stacks])


def move_crates(stacks: list[list[str]], num, from_stack, to_stack):
    for _ in range(num):
        stacks[to_stack-1].append(stacks[from_stack-1].pop())


def move_multiple_crates(stacks: list[list[str]], num, from_stack, to_stack):
    stacks[to_stack-1].extend(stacks[from_stack-1][-num:])
    stacks[from_stack-1] = stacks[from_stack-1][:-num]


with open('input.txt') as f:
    stacks_txt, procedure = [txt.splitlines() for txt in f.read().split('\n\n')]

stacks = create_stacks(stacks_txt)
ans = get_top_rearrange_stacks(stacks, move_crates)
print(f"part 1 answer: {ans}")

stacks = create_stacks(stacks_txt)
ans = get_top_rearrange_stacks(stacks, move_multiple_crates)
print(f"part 2 answer: {ans}")
end_time = time.time()
print(f"Time: {round((end_time-start_time)*1000, 4)}ms")



