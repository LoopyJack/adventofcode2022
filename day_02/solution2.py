
shapes = ['r', 'p', 's']
opponent = dict(zip(['A', 'B', 'C'], shapes))
player   = dict(zip(['X', 'Y', 'Z'], shapes))
shape_score = dict(zip(shapes, [1, 2, 3]))


game_score = {
    'r': {
        'r': 3 + shape_score['r'],
        'p': 6 + shape_score['p'],
        's': 0 + shape_score['s']
    },
    'p': {
        'r': 0 + shape_score['r'],
        'p': 3 + shape_score['p'],
        's': 6 + shape_score['s']
    },
    's': {
        'r': 6 + shape_score['r'],
        'p': 0 + shape_score['p'],
        's': 3 + shape_score['s']
    }
}


with open('./day_02/input.txt') as f:
    games = [tuple(game.split()) for game in f.read().splitlines()]

total_score = sum([game_score[opponent[game[0]]][player[game[1]]] for game in games])
print(f"part 1 answer: {total_score}")

########## Part 2 ##########

total_score = 0
for game in games:
    if game[1] == 'X': # lose
        if   opponent[game[0]] == 'r': total_score += game_score['r']['s']
        elif opponent[game[0]] == 'p': total_score += game_score['p']['r']
        elif opponent[game[0]] == 's': total_score += game_score['s']['p']
    elif game[1] == 'Y': # draw
        if   opponent[game[0]] == 'r': total_score += game_score['r']['r']
        elif opponent[game[0]] == 'p': total_score += game_score['p']['p']
        elif opponent[game[0]] == 's': total_score += game_score['s']['s']
    elif game[1] == 'Z': # win
        if   opponent[game[0]] == 'r': total_score += game_score['r']['p']
        elif opponent[game[0]] == 'p': total_score += game_score['p']['s']
        elif opponent[game[0]] == 's': total_score += game_score['s']['r']

print(f"part 2 answer: {total_score}")
