

class Point:
    def __init__(self, y, x):
        self.y = y
        self.x = x

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self) -> str:
        return f'({self.y}, {self.x})'

    __str__ = __repr__


class Shape:
    def __init__(self, txt: str, letter: str):
        self.letter = letter 
        self.points = list[Point]()
        for y, row in enumerate(txt.splitlines()):
            for x, col in enumerate(row):
                if col == '#':
                    self.points.append(Point(-y, x)) #= reverse y axis

        self.min_x = min([p.x for p in self.points])
        self.max_x = max([p.x for p in self.points])
        self.min_y = min([-p.y for p in self.points])
        self.max_y = max([-p.y for p in self.points])
        self.height = self.max_y - self.min_y + 1

    def draw(self):
        ret = ''
        for y in range(self.max_y + 1):
            for x in range(self.max_x + 1):
                if Point(y, x) in self.points:
                    ret += self.letter
                else:
                    ret += '.'
            ret += '\n'
        print(ret)
        

class Rock:
    def __init__(self, shape: Shape, location: Point):
        self.shape = shape
        self.location = location
        self.occupied_space = [Point(p.y + self.location.y, p.x + self.location.x) for p in self.shape.points]

    def move(self, direction: str):
        if direction == '>':
            self.location.x += 1    
        elif direction == '<':
            self.location.x -= 1
        elif direction == '^':
            self.location.y += 1
        elif direction == 'v':
            self.location.y -= 1
        self.occupied_space = [Point(p.y + self.location.y, p.x + self.location.x) for p in self.shape.points]

    @property
    def max_y(self):
        return max([p.y for p in self.occupied_space])
    @property
    def min_y(self):
        return min([p.y for p in self.occupied_space])

    def __str__(self) -> str:
        return f'{self.shape.draw()} at {self.location}'


class Chamber:
    def __init__(self, width: int, extra_height: int):
        self.width = width
        self.extra_height = extra_height
        self.space = []
        self.rocks = []
        self._height = 0
        self.height = extra_height
        self.highest_point = 0


    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, value: int):
        height_diff = value - self._height
        if height_diff > 0:
            for _ in range(height_diff):
                # print('increasing height')
                self.space.append([None]*self.width)
        self._height = value

    def create_rock(self, shape: Shape):
        rock = Rock(shape, Point(self.height-1, 2))
        gap = rock.min_y - self.highest_point
        if gap < self.extra_height:
            self.height += self.extra_height - gap
            for _ in range(self.extra_height - gap):
                rock.move('^')
        elif gap > self.extra_height:
            for _ in range(gap - self.extra_height):
                rock.move('v')
        for point in rock.occupied_space:
            self.space[point.y][point.x] = rock
        # self.rocks.append(rock)
        return rock

    def add_rock(self, rock: Rock):
        for point in rock.occupied_space:
            self.space[point.y][point.x] = rock
        # self.rocks.append(rock)

    def remove_rock(self, rock: Rock):
        for point in rock.occupied_space:
            self.space[point.y][point.x] = None
        # self.rocks.remove(rock)

    def move_rock(self, rock: Rock, direction: str):
        next_position = translated_position(rock.occupied_space, direction)
        for point in next_position:
            if point.y > self.height or point.y < 0 or point.x >= self.width or point.x < 0:
                return False
            if self.space[point.y][point.x] is not None and self.space[point.y][point.x] != rock:
                return False
        self.remove_rock(rock)
        rock.move(direction)
        self.add_rock(rock)
        return True

    def draw(self, rows=None, header=None):
        ret = '' if header is None else header + '\n'
        lines = reversed(self.space[-rows:]) if rows is not None else reversed(self.space)
        for i, row in enumerate(lines):
            ret += '|'
            for col in row:
                if col is None:
                    ret += '.'
                else:
                    ret += col.shape.letter
            ret += f'|{self.height-i}\n'
        ret += '+' +'-'*self.width + '+\n\n'
        print(ret)


def translated_position(points: list[Point], direction: str):
    ret = []
    if direction == '<':
        for point in points:
            ret.append(Point(point.y, point.x - 1))
    elif direction == '>':
        for point in points:
            ret.append(Point(point.y, point.x + 1))
    elif direction == '^':
        for point in points:
            ret.append(Point(point.y + 1, point.x))
    elif direction == 'v':
        for point in points:
            ret.append(Point(point.y - 1, point.x))
    return ret


def parse_shapes():
    with open('./day_17/rocks.txt') as f:
        shapes = [Shape(d, chr(97+i)) for i, d in enumerate(f.read().split('\n\n'))]
    return shapes

def parse_moves():
    with open('./day_17/input.txt') as f:
        data = list(f.read())
        moves = []
        for d in data:
            moves.append(d)
            moves.append('v')
    return moves



width = 7
extra_height = 3
chamber = Chamber(width, extra_height)


num_rocks = 1000000000000

shapes = parse_shapes()
moves = parse_moves()
cur_shape = shapes.pop(0)
for i in range(num_rocks):
    if i % 1000 == 0:
        print(f'{i / num_rocks}')
    rock = chamber.create_rock(cur_shape)
    # chamber.draw(header=f'new rock')
    direction = moves.pop(0)


    while chamber.move_rock(rock, direction) or direction != 'v':
        # chamber.draw(header=f'moved {direction}')
        moves.append(direction)
        direction = moves.pop(0)

    if rock.max_y+1 > chamber.highest_point:
        chamber.highest_point = rock.max_y+1
        # print(f'height: {chamber.height}')
        # chamber.draw()
    shapes.append(cur_shape)
    cur_shape = shapes.pop(0)
    moves.append(direction)


chamber.draw()
print(chamber.highest_point)
pass
    
