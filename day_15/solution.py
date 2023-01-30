class SensorMap():
    def __init__(self, sensor_locs):
        self.sensor_locs = sensor_locs

    def count_coverage_of_row(self, y_idx):
        locations = set()
        for sensor_loc in self.sensor_locs:
            for scan_loc in scan_sensor_row(sensor_loc, y_idx):
                locations.add(scan_loc[1])
        for beacon_loc in self.sensor_locs:
            _, _, b_x, b_y = beacon_loc
            if b_y == y_idx and b_x in locations:
                locations.remove(b_x)
        return len(locations)

    def get_all_sensor_ranges_for_row(self, y):
        ranges = []
        for sensor in self.sensor_locs:
            r = get_sensor_row_boundaries(sensor, y)
            if r is not None: ranges.append(r)
        ranges.sort(key=lambda x: (x[0], x[1]))
        return ranges

    def search_area_for_gaps(self, boundary: int):
        for y in range(boundary+1):
            sensor_ranges = consolidate_ranges(self.get_all_sensor_ranges_for_row(y))
            if len(sensor_ranges) > 1:
                for i in range(1, len(sensor_ranges)):
                    # print(f"row: {y}, gap: {sensor_ranges[i-1][1]+1}-{sensor_ranges[i][0]-1}")
                    return (sensor_ranges[i-1][1]+1, y)

def consolidate_ranges(ranges):
    res = [ranges.pop(0)]
    while len(ranges) > 0:
        if ranges[0][0] >= res[-1][0] and ranges[0][1] <= res[-1][1]: # right contained in left
            ranges.pop(0)
        elif ranges[0][0] <= res[-1][1]+1 and ranges[0][1] > res[-1][1]: # right overlaps left
            res[-1][1] = ranges[0][1]
            ranges.pop(0)
        else: # ranges are gapped
            res.append(ranges.pop(0))
    return res

def scan_sensor_area(sensor_loc):
    s_x, s_y, b_x, b_y = sensor_loc
    x_dist = abs(s_x - b_x)
    y_dist = abs(s_y - b_y)
    dist = x_dist + y_dist
    for y in range(-dist, dist +1):
        for x in range(-(dist - abs(y)), +(dist - abs(y)) +1):
            yield (s_y - y, s_x + x)

def scan_sensor_row(sensor_loc, y_idx):
    s_x, s_y, b_x, b_y = sensor_loc
    x_dist = abs(s_x - b_x)
    y_dist = abs(s_y - b_y)
    dist = x_dist + y_dist
    if y_idx not in range(s_y-dist, s_y+dist+1):
        return
    y = y_idx - s_y
    for x in range(-(dist - abs(y)), +(dist - abs(y)) +1):
        yield (y_idx, s_x + x)

def get_sensor_row_boundaries(sensor_loc, y_idx):
    s_x, s_y, b_x, b_y = sensor_loc
    x_dist = abs(s_x - b_x)
    y_dist = abs(s_y - b_y)
    dist = x_dist + y_dist
    if y_idx not in range(s_y-dist, s_y+dist+1):
        return
    y = y_idx - s_y
    return [s_x + -(dist - abs(y)), s_x + (dist - abs(y)) ]

data = []
with open('./day_15/input.txt') as f:
    lines = f.read().splitlines()
    for line in lines:
        _, _, s_x, s_y, _, _, _, _, b_x, b_y = line.split()
        data.append((
            int(s_x.split('=')[1][:-1]), # sensor x
            int(s_y.split('=')[1][:-1]), # sensor y
            int(b_x.split('=')[1][:-1]), # beacon x
            int(b_y.split('=')[1]     )  # beacon y
        ))

scan_y = 2000000
s_map = SensorMap(data)
ans = s_map.count_coverage_of_row(scan_y)
print(f"part 1: {ans}")

boundary = 4000000
gap = s_map.search_area_for_gaps(boundary)
ans = (gap[0]*boundary) + gap[1]
print(f"part 2: {ans}")