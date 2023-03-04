scores = {
    'A X': 1+3,
    'A Y': 2+6,
    'A Z': 3+0,
    'B X': 1+0,
    'B Y': 2+3,
    'B Z': 3+6,
    'C X': 1+6,
    'C Y': 2+0,
    'C Z': 3+3
}

with open("input.txt", "r") as f:
    data = f.read().split("\n")

# Part 1
total_score = sum([scores[game] for game in data])
print(f"Part 1 answer: {total_score}")

# Part 2
strategies = { # dict of intended outcomes
    'X': { # losers
        'A': 'Z',
        'B': 'X',
        'C': 'Y'
    },
    'Y': { # draws
        'A': 'X',
        'B': 'Y',
        'C': 'Z'
    },
    'Z': { # winners
        'A': 'Y',
        'B': 'Z',
        'C': 'X'
    }
}

revised_games = [f"{game[0]} {strategies[game[2]][game[0]]}" for game in data]
total_score = sum([scores[game] for game in revised_games])
print(f"Part 2 answer: {total_score}")





