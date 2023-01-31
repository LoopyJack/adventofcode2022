

class Monkey:
    def __init__(self, line: str):
        self.name, data = line.split(':')

        try:
            self.data = int(data)
            self.shout = self._data
        except:
            self._m1, self._op, self._m2 = data.split()
            self.shout = self._operate


    def _data(self):
            return self.data

    def _operate(self):
        m1 = float(monkies[self._m1].shout())
        m2 = float(monkies[self._m2].shout())
        if self._op == '+':
            return m1 + m2
        elif self._op == '-':
            return m1 - m2
        elif self._op == '*':
            return m1 * m2
        if self._op == '/':
            return m1 / m2
        if self._op == '=':
            print(f"m1: {m1}   m2: {m2}")
            return m1 == m2

monkies = {}
with open('input.txt') as f:
    data = f.read().splitlines()
    for d in data:
        name = d.split(':')[0]
        monkies[name] = Monkey(d)

print(f"part 1 answer: {int(monkies['root'].shout())}")


########### Part 2 ###########


monkies['root']._op = '='
monkies['humn'].shout = input

print(monkies['root'].shout())


