def find_start_idx(start_length: int, message: str):
    for i, _ in enumerate(message):
        chars = {char: True for char in message[i:i+start_length]}
        if len(chars) == start_length:
            return i+start_length

with open('./day_06/input.txt') as f:
    message = f.read()

ans = find_start_idx(4, message)
print(f"Part 1: {ans}")

ans = find_start_idx(14, message)
print(f"Part 2: {ans}")

