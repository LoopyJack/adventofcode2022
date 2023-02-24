
X = 0
Y = 1

terrain = []
blizzards = []
walls = {
    'top': 0,
    'left': 0 
}
with open('input.txt') as f:
    lines = f.read().splitlines()
    entrance = (lines[0].index('.'), 0)
    exit = (lines[-1].index('.'), len(lines)-1)
    for y, line in enumerate(lines):
        row = [0] * len(line)
        for x, char in enumerate(line):
            if char in ['>', 'v', '<', '^']:
                blizzards.append([x, y, char])
                row[x] += 1
        terrain.append(row)
walls['bottom'] = len(terrain) - 1        
walls['right' ] = len(terrain[0]) - 1


expedition = (entrance[X], entrance[Y])

def pt(terrain, blizzards):
    pic = [['#']*len(terrain[0])]
    pic[0][entrance[X]] = '.'
    for y, row in enumerate(terrain[1:-1]):
        pic_row = ['#']
        for x, col in enumerate(row[1:-1]):
            if col > 1: 
                pic_row.append(str(col))
            elif col == 1:
                for b in blizzards:
                    if b[0]-1 == x and b[1]-1 == y:
                        pic_row.append(b[2])
                        break
            else: 
                pic_row.append('.')
        pic_row.append('#')
        pic.append(pic_row)
    pic.append(['#']*len(terrain[-1]))
    pic[-1][exit[X]] = '.'
    pic[expedition[Y]][expedition[X]] = 'E'
    # for r in pic:
    #     print(''.join(r))
    return pic


def move_blizzards(terrain, blizzards, walls):
    for b in blizzards:
        terrain[b[1]][b[0]] -= 1
        if b[2] == '>':
            b[0] += 1
            if b[0] == walls['right']: 
                b[0] = 1    
        elif b[2] == 'v':
            b[1] += 1
            if b[1] == walls['bottom']: 
                b[1] = 1
        elif b[2] == '<':
            b[0] -= 1
            if b[0] == walls['left']: 
                b[0] = walls['right'] - 1
        elif b[2] == '^':
            b[1] -= 1
            if b[1] == walls['top']: 
                b[1] = walls['bottom'] - 1
        terrain[b[1]][b[0]] += 1

def move_expedition(terrain, expedition, exit):
    x_dist = exit[X] - expedition[X]
    y_dist = exit[Y] - expedition[Y]
    move_preferences = []
    if x_dist > y_dist: # x is greater so horizontal move
        if y_dist > 1:
            move_preferences = [(1,0), (0,1), (0,0), (0,-1), (-1, 0)]
        else: 
            move_preferences = [(1,0), (0,0), (0,-1), (-1, 0)]
    elif x_dist <= y_dist: # y is greater so vertical move
        if x_dist > 0:
            move_preferences = [(0,1), (1,0), (0,0), (-1,0), (0, -1)]
        else:
            move_preferences = [(0,1), (0,0), (-1,0), (0, -1)]

    for move in move_preferences:
        if terrain[expedition[Y]+move[Y]][expedition[X]+move[X]] == 0:
            new_position = (expedition[X]+move[X], expedition[Y]+move[Y])
            return new_position
    else:
        for p in pt(terrain, blizzards):
            print(''.join(p))
    



rnd = 0
while expedition != exit:
    pic = pt(terrain, blizzards)
    # for p in pic:
    #     print(''.join(p))
    # print(blizzards)
    move_blizzards(terrain, blizzards, walls)
    expedition = move_expedition(terrain, expedition, exit)
    rnd += 1
    print(f'\nround: {rnd}')
