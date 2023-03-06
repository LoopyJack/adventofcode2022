import time
start_time = time.perf_counter()
def find_start_idx(start_length: int, message: str):
    i = start_length-1
    while i < len(message):
        chars = set()
        j = i
        while j >= i - start_length:
            if message[j] in chars:
                i = j + start_length-1
                break
            if j == i-start_length+1:
                return i+1
            chars.add(message[j])
            j -= 1
        i += 1

with open('input.txt') as f:
    message = f.read()

ans = find_start_idx(4, message)
print(f"Part 1 answer: {ans}")

ans = find_start_idx(14, message)
print(f"Part 2 answer: {ans}")
end_time = time.perf_counter()
print(f"Time: {round((end_time-start_time)*1000, 4)}ms")