from collections import deque, defaultdict

Location = tuple[int, int]


HEIGHT_CAN_CLIMB = 1
POSSIBLE_DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


class Graph:

    def __init__(self, terrain: list[list[str]]):
        
        self.start_loc = None
        self.end_loc = None
        self._terrain: list[list[str]]
        self.neighbors = defaultdict[Location, list[Location]]()
        
        self.terrain = terrain


    def process_terrain(self):
        """
        Generate neighbors for all nodes and find start/end locations
        """
        for y in range(len(self._terrain)):
            for x in range(len(self._terrain[y])):
                if self._terrain[y][x] == 'S':
                    self.start_loc = (y, x)
                elif self._terrain[y][x] == 'E':
                    self.end_loc = (y, x)
                self.neighbors[(y, x)] = self.get_neighbors((y, x))
            


    def get_neighbors(self, node: Location) -> list[Location]:
        neighbors = []

        for direction in POSSIBLE_DIRECTIONS:
            y_neighbor = node[0] + direction[0]
            x_neighbor = node[1] + direction[1]

            # neighbor is out of bounds
            if x_neighbor < 0 or x_neighbor >= len(self._terrain[node[0]]) or \
            y_neighbor < 0 or y_neighbor >= len(self._terrain):
                continue

            h_neighbor = self._terrain[y_neighbor][x_neighbor]
            if h_neighbor == 'S': h_neighbor = 'a' 
            elif h_neighbor == 'E': h_neighbor = 'z'

            h_node = self._terrain[node[0]][node[1]]
            if h_node == 'S': h_node = 'a' 
            elif h_node == 'E': h_node = 'z'

            if ord(h_neighbor) - ord(h_node) <= HEIGHT_CAN_CLIMB:
                neighbors.append((y_neighbor, x_neighbor))
            
        return neighbors


    def breadth_first_search(self):
        step_count = 0
        if not self.start_loc or  not self.end_loc:
            return
        frontier = deque()
        came_from = dict[Location, Location]()
        frontier.append(self.start_loc)
        came_from[self.start_loc] = None
        while frontier:
            step_count += 1
            loc = frontier.popleft()
            if loc == self.end_loc:
                break
            for neighbor in self.neighbors[loc]:
                if neighbor not in came_from:
                    frontier.append(neighbor)
                    came_from[neighbor] = loc

        if self.end_loc not in came_from:
            return {
                'path': None, 
                'steps': step_count
            }
        path = [self.end_loc]
        while came_from[path[-1]] != self.start_loc:
                path.append(came_from[path[-1]])  
        path.reverse()
        return {
            'path': path,
            'steps': step_count
        }

    def get_height_locs(self, height: str):
        return [(y, x) for y, row in enumerate(terrain) for x, col in enumerate(row) if col == height]



    
    def print(self):
        self._print_terrain(self.terrain)

    def print_path(self, path: list[Location]):

        terrain = self.terrain.copy()
        for loc in path:
            terrain[loc[0]][loc[1]] = '.'
        self._print_terrain(terrain)
        print(f"steps: {len(path)}")
        
    def _print_terrain(self, terrain):
        res =''
        for row in terrain:
            for col in row:
                res += col
            res += '\n'
        print(res)

    def describe(self):
        print(f"x size: {len(self.terrain[0])}, y size: {len(self.terrain)}, nodes {len(self.terrain[0])*len(self.terrain)}")
        print(f"start location: {self.start_loc}")
        print(f"end location: {self.end_loc}")



    @property 
    def terrain(self):
        return self._terrain

    @terrain.setter
    def terrain(self, value):
        self._terrain = value
        self.process_terrain()
    




with open('./day_12/input.txt') as f:
    terrain = [list(row) for row in f.read().splitlines()]

g = Graph(terrain)
x = g.breadth_first_search()
g.print_path(x['path'])
start_locs = [g.start_loc] + g.get_height_locs('a')

results = []
for start_loc in start_locs:
    g.start_loc = start_loc
    res = g.breadth_first_search()
    if res['path'] is not None:
        results.append((start_loc, len(res['path'])))

results.sort(key=lambda x: x[1])