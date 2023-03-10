import time
start_time = time.perf_counter()
def find_start_idx(start_length: int, message: str):
    for i in range(len(message)):
        if len(set(message[i:i+start_length])) == start_length:
            return i+start_length

with open('input.txt') as f:
    message = f.read()

ans = find_start_idx(4, message)
print(f"Part 1 answer: {ans}")

ans = find_start_idx(14, message)
print(f"Part 2 answer: {ans}")
end_time = time.perf_counter()
print(f"Time: {round((end_time-start_time)*1000, 4)}ms")