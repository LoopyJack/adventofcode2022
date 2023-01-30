from dataclasses import dataclass

@dataclass
class BodyPart:
    pos: int
    x: int
    y: int
    last_move: str = None

def count_locations_visited(num_body_parts, max_apart):

    locations_visited = {(0,0)}
    body_segments = []
    for i in range(num_body_parts):
        body_segments.append(BodyPart(i, 0, 0))

    with open('./day_09/input.txt') as f:
        movements = f.read().splitlines()

    for movement in movements:
        direction = movement[0]
        distance = int(movement[1:])

        for _ in range(distance):
            if direction == 'R':
                body_segments[0].x += 1
            elif direction == 'L':
                body_segments[0].x -= 1
            elif direction == 'U':
                body_segments[0].y += 1
            elif direction == 'D':
                body_segments[0].y -= 1
            body_segments[0].last_move = direction
            
            for i in range(1,len(body_segments)):
                diff_x = body_segments[i-1].x - body_segments[i].x
                diff_y = body_segments[i-1].y - body_segments[i].y

                if abs(diff_x) > max_apart:
                    sign = 1 if diff_x > 0 else -1
                    body_segments[i].x += 1 * sign
                    if diff_y != 0:
                        sign = 1 if diff_y > 0 else -1
                        body_segments[i].y += 1 * sign
                elif abs(diff_y) > max_apart:
                    sign = 1 if diff_y > 0 else -1
                    body_segments[i].y += 1 * sign
                    if diff_x != 0:
                        sign = 1 if diff_x > 0 else -1
                        body_segments[i].x += 1 * sign

                if i == len(body_segments)-1:
                        locations_visited.add((body_segments[i].x, body_segments[i].y))
    return len(locations_visited)


print(f"Part 1: {count_locations_visited(2, 1)}")
print(f"Part 2: {count_locations_visited(10, 1)}")

