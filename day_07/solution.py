with open('example.txt') as f:
    lines = f.read().splitlines()

directories = ['/']
files = {'/' : []}
cwd = ''

def cd(dir, cwd):
    if dir == '..':
       chdir = cwd[:-1].rsplit('/', 1)[0]+'/'
    elif dir == '/':
        chdir = '/'
    else:
        chdir = cwd+dir+'/'
        if chdir not in directories:
            raise Exception('Directory does not exist')
    return chdir

for idx, line in enumerate(lines):
    if line[0] == '$':
        cmd = line[2:4]
        if cmd == 'cd':
            dir = line[5:]
            cwd = cd(dir, cwd)
        else:
            pass # don't need to handle ls yet
    else: # it's a file
        if line[:3] == 'dir':
            new_dir = cwd+line[4:]+'/'
            if new_dir not in directories:
                directories.append(new_dir)
                files[new_dir] = []
            else:
                print('Directory already exists')
        else:
            size, file_name = line.split(' ')
            files[cwd].append([int(size), file_name])

directories.sort()
sums = {}
rec_sizes = {}

for directory, dir_files in files.items():
    total = 0
    for file in dir_files:
        total += file[0]
    sums[directory] = total

for idx, d in enumerate(directories):
    rec_size = 0
    for idx2 in range(idx, len(directories)):
        if directories[idx2].startswith(d):
            rec_size += sums[directories[idx2]]
    rec_sizes[d] = rec_size

#### Part 1
ans1 = 0
for rec_size in rec_sizes.values():
    if rec_size < 100000:
        ans1 += rec_size
print(f"Part 1 answer: {ans1}")


### Part 2
disk_size = 70000000
space_remaining = disk_size-sum(sums.values())
size_to_delete = 30000000 - space_remaining

# find the smallest directory greater than size_to_delete:
candidates = []
for k, v in rec_sizes.items():
    if v > size_to_delete:
        candidates.append({k:v})
candidates.sort(key=lambda x: list(x.values())[0])
ans2 = list(candidates[0].values())[0]
print(f"Part 2 answer: {ans2}")

        