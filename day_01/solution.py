

with open('./day_01/data.txt') as f:
    data = f.read()

print('part 1:', max([sum(list(map(int,d.split('\n')))) for d in data.split('\n\n')]))
print('part 2:', sum(sorted([sum(list(map(int,d.split('\n')))) for d in data.split('\n\n')])[-3:]))
    