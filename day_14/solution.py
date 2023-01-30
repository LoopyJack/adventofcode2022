# guesses 27156


with open('./day_14/input.txt') as f:
    rocks = [[tuple([int(coord) for coord in point.split(',')]) for point in rock.split(' -> ')] for rock in f.read().splitlines()]

class Cave:
    def __init__(self, rocks):
        self.rocks = rocks
        self.sand_count = 0
        self.plot_rocks(rocks)


    def plot_rocks(self, rocks: list[list[tuple]]) -> list[list[str]]:

        X_MIN = min([point[0] for rock in rocks for point in rock]) 
        X_MAX = max([point[0] for rock in rocks for point in rock]) 
        Y_MIN = min([point[1] for rock in rocks for point in rock]) 
        Y_MAX = max([point[1] for rock in rocks for point in rock]) 

        self.x_offset = X_MIN - 1
        # self.y_offset = Y_MIN - 1

        model = [['.']*(X_MAX-X_MIN+3) for _ in range(Y_MAX+2)]

        for rock in rocks:
            last_corner = None
            for corner in rock:
                if last_corner is None: 
                    last_corner = corner
                    continue
                
                if last_corner[0] == corner[0]: # vertical line
                    min_idx = min(last_corner[1], corner[1])
                    max_idx = max(last_corner[1], corner[1])
                    for y in range(min_idx, max_idx):
                        model[y][corner[0]-self.x_offset] = '#'
                else: # horizontal line
                    min_idx = min(last_corner[0], corner[0])
                    max_idx = max(last_corner[0], corner[0])
                    for x in range(min_idx, max_idx+1):
                        model[corner[1]][x-self.x_offset] = '#'

                last_corner = corner
        self.model = model    

    def add_foor(self):
        self.model.append(['#']*len(self.model[0]))

    def expand_left(self):
        for i, row in enumerate(self.model):
            char = '.' if i != len(self.model) - 1 else '#'
            self.model[i] = [char] + row
        self.x_offset -= 1

    def expand_right(self):
        for i, row in enumerate(self.model):
            char = '.' if i != len(self.model) - 1 else '#'
            self.model[i] = row + [char]


    def drop_sand(self):
        sand_loc = [500-self.x_offset, 0]

        x = sand_loc[0]
        y = sand_loc[1]
        while y+1 < len(self.model) and self.model[y][x] != 'o':
            if self.model[y+1][x] == '.': # straight down
                y += 1
            elif self.model[y+1][x] != '.':
                if x - 1 == 0: 
                    x += 1
                    self.expand_left()
                if x + 1 == len(self.model[y+1]) - 1: self.expand_right()
                if self.model[y+1][x-1] == '.': # diagonal left
                    y += 1
                    x -= 1
                elif self.model[y+1][x+1] == '.': # diagonal right
                    y += 1
                    x += 1
                else: # stop falling
                    self.model[y][x] = 'o'
                    self.sand_count += 1
                    return True
        return False
            
    def stack_sand(self):
        while self.drop_sand():
            pass
        return self.sand_count

    def draw(self):
        res = ''
        for row in self.model:
            res += ''.join(row)+'\n'
        print(res)


cave = Cave(rocks)
cave.stack_sand()
ans = cave.stack_sand()
print(f"part 1: {ans}")

cave = Cave(rocks)
cave.add_foor()
ans = cave.stack_sand()
print(f"part 2: {ans}")



