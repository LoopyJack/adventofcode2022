from dataclasses import dataclass

@dataclass
class Cell:
    x: int
    y: int
    height: int
    vis_from_left: bool = False
    vis_from_right: bool = False
    vis_from_top: bool = False
    vis_from_bottom: bool = False
    area: int = 0



def look_right(cell):
    i = 0
    for i in range(1, len(grid[cell.y])-cell.x):
        print(i)
        if grid[cell.y][cell.x+i].height >= cell.height:
            break
    return i


def look_left(cell):
    i = 0
    for i in range(1, cell.x+1):
        if grid[cell.y][cell.x-i].height >= cell.height:
            break
    return i

def look_up(cell):
    i = 0
    for i in range(1, cell.y+1):
        if grid[cell.y-i][cell.x].height >= cell.height:
            break
    return i

def look_down(cell):
    i = 0
    for i in range(1, len(grid)-cell.y):
        if grid[cell.y+i][cell.x].height >= cell.height:
            break
    return i


def calc_area(cell):
    return look_right(cell) * look_left(cell) * look_up(cell) * look_down(cell)



with open('./day_08/input.txt') as f:
    big_string = f.read()



grid = []

for i, line in enumerate(big_string.splitlines()):
    grid.append([])
    for j, char in enumerate(line):
        grid[i].append(Cell(j, i, int(char)))


# visible from left:
for i, row in enumerate(grid):
    max_height = 0
    for j, cell in enumerate(row):
        if cell.height > max_height or i == 0 or j == 0:
            cell.vis_from_left = True
            max_height = cell.height

# visible from right:
for i, row in enumerate(grid):
    max_height = 0
    for j, cell in enumerate(row[::-1]):
        if cell.height > max_height or i == 0 or j == 0:
            cell.vis_from_right = True
            max_height = cell.height

# visible from top:
for j, col in enumerate(zip(*grid)):
    max_height = 0
    for i, cell in enumerate(col):
        if cell.height > max_height or i == 0 or j == 0:
            cell.vis_from_top = True
            max_height = cell.height

# visible from bottom:
for j, col in enumerate(zip(*grid)):
    max_height = 0
    for i, cell in enumerate(col[::-1]):
        if cell.height > max_height or i == 0 or j == 0:
            cell.vis_from_bottom = True
            max_height = cell.height


# count visible cells:
visible_cells = 0
for row in grid:
    for cell in row:
        cell.area = calc_area(cell)
        if cell.vis_from_left or cell.vis_from_right or cell.vis_from_top or cell.vis_from_bottom:
            visible_cells += 1




#find cell with max area:
max_area = 0
for row in grid:
    for cell in row:
        if cell.area > max_area:
            print(cell)
            max_area = cell.area
            



print(visible_cells)
print(max_area)
