def calc_score(commons):
    ans  = sum([ord(char)-96 for char in commons if char.islower()]) 
    ans += sum([ord(char)-38 for char in commons if char.isupper()])
    return ans


with open("./day_03/input.txt") as f:
    lines = f.read().splitlines()


# Part 1
commons = [(set(line[:len(line)//2]) & set(line[len(line)//2:])).pop() for line in lines]
print(f"part 1: {calc_score(commons)}")


# Part 2
commons = [(set(lines[i]) & set(lines[i+1]) & set(lines[i+2])).pop() for i in range(0,len(lines),3)]
print(f"part 2: {calc_score(commons)}")