
numerals = ['2', '1', '0', '-', '=']

def parse_input(file):
    with open(file) as f:
        return [list(x.strip()) for x in f.read().splitlines()]


def to_decimal(snafu):
    snafu = list(map(lambda x: x.replace('-', '-1').replace('=', '-2'), reversed(snafu)))
    return sum(5**i*int(s) for i, s in enumerate(snafu))


def to_snafu(dec):
    snafu = ['2']
    while to_decimal(snafu) < dec:
        snafu.append('2')
    new_snafu = snafu.copy()
    for i in range(1, len(snafu)):
        for j, n in enumerate(numerals[1:]):
            new_snafu[i] = n
            new_dec = to_decimal(new_snafu)
            if  new_dec < dec:
                new_snafu[i] = numerals[j]
                new_dec = to_decimal(new_snafu)
                break
            elif new_dec == dec:
                return ''.join(new_snafu)


raw = parse_input('input.txt')
total = sum([to_decimal(r) for r in raw])
ans1 = to_snafu(total)
print(f"answer to part 1: {ans1}")

