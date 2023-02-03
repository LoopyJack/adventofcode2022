from collections import deque


with open('./example.txt') as f:
    data_board, data_directions = f.read().split('\n\n')
    board = [[c for c in line] for line in data_board.split('\n')]
    directions = data_directions.replace('L', ' L ').replace('R', ' R ').split()


def uniform_board(board):
    res = []
    max_x = max(len(b) for b in board)
    for b in board:
        b = b if len(b) == max_x else b + [' '] * (max_x - len(b))
        res.append(b)
    return res

#board[y][x]
board = uniform_board(board)
traveled = [b.copy() for b in board]

facing = deque(['>', 'v', '<', '^'])
rotate = { 'R': -1, 'L': 1 }
moves = deque([(0, 1), (1, 0), (0, -1), (-1, 0)])
face_score = {
    (0, 1) : 0, 
    (1, 0) : 1,
    (0, -1): 2,
    (-1, 0): 3
}
chevron = {
    (0, 1) : '>', 
    (1, 0) : 'v',
    (0, -1): '^',
    (-1, 0): '<'
}


loc = (0, 0)
for y, row in enumerate(board):
    for x, char in enumerate(row):
        if char == '.':
            loc = (y, x)
            break
    else:
        continue
    break

print(directions)
print(f"start: {loc}")

while directions:
    action = directions.pop(0)
    if action in ['L', 'R']:
        moves.rotate(rotate[action])
    else:
        action = int(action)
        for _ in range(action):
            next_loc = (loc[0]+moves[0][0], loc[1]+moves[0][1])
            wrap_loc = None

            # check move up
            if moves[0] == (-1, 0) and (next_loc[0] < 0 or board[next_loc[0]][next_loc[1]] == ' '):
                wrap_loc = loc
                moves.rotate(2)
                while True:
                    if wrap_loc[0] < len(board)-1 and board[wrap_loc[0]+moves[0][0]][wrap_loc[1]+moves[0][1]] != ' ':
                        wrap_loc = (wrap_loc[0]+moves[0][0], wrap_loc[1]+moves[0][1])
                    else: break
                moves.rotate(2)

            #check move right
            if moves[0] == (0, 1) and (next_loc[1] >= len(board[next_loc[0]]) or board[next_loc[0]][next_loc[1]] == ' '):
                wrap_loc = loc
                moves.rotate(2)
                while True:
                    if wrap_loc[1] > 0 and board[wrap_loc[0]+moves[0][0]][wrap_loc[1]+moves[0][1]] != ' ':
                        wrap_loc = (wrap_loc[0]+moves[0][0], wrap_loc[1]+moves[0][1])
                    else: break
                moves.rotate(2)
            
            # check move down
            if moves[0] == (1, 0) and (next_loc[0] >= len(board) or board[next_loc[0]][next_loc[1]] == ' '):
                wrap_loc = loc
                moves.rotate(2)
                while True:
                    if wrap_loc[0] > 0 and board[wrap_loc[0]+moves[0][0]][wrap_loc[1]+moves[0][1]] != ' ':
                        wrap_loc = (wrap_loc[0]+moves[0][0], wrap_loc[1]+moves[0][1])
                    else: break
                moves.rotate(2)

            #check move left
            if moves[0] == (0, -1) and (next_loc[1] < 0 or board[next_loc[0]][next_loc[1]] == ' '):
                wrap_loc = loc
                moves.rotate(2)
                while True:
                    if wrap_loc[1] < len(board[wrap_loc[0]])-1 and board[wrap_loc[0]+moves[0][0]][wrap_loc[1]+moves[0][1]] != ' ':
                        wrap_loc = (wrap_loc[0]+moves[0][0], wrap_loc[1]+moves[0][1])
                    else: break
                moves.rotate(2)

            if wrap_loc: next_loc = wrap_loc

            if board[next_loc[0]][next_loc[1]] == '#':
                break 

            loc = next_loc
            traveled[loc[0]][loc[1]] = chevron[moves[0]]
        
ans = 1000 * (loc[0]+1) + 4 * (loc[1]+1) + face_score[moves[0]]
print(f"answer to part 1: {ans}")            


# for t in board:
#     print(''.join(t))

############### Part 2 ###############
edge_length = 4
sides = []
rows = len(board) // edge_length
cols = len(board[0]) // edge_length

for r in range(rows):
    for c in range(cols):
        idx = (r * (rows+1)) + c
        print(idx, r, c)
        # for row in board[r*edge_length:(r*edge_length)+edge_length]:
        #     for char in row[c*edge_length:(c*edge_length)+edge_length]:
        #         print(len(row[c*edge_length:(c*edge_length)+edge_length]), char)
        sides.append([[char for char in row[c*edge_length:(c*edge_length)+edge_length]] for row in board[r*edge_length:(r*edge_length)+edge_length]])




for s in sides:
    for r in s:
        print(r)
    print()




