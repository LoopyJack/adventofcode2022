from fast_divide_check import *

class Monkey:
    def __init__(self, input_str: str):
        lines = input_str.splitlines()
        for line in lines:
            if line.strip().startswith('Monkey'):
                self.num = int(line[-2])
            elif line.strip().startswith('Starting items'):
                items = line.split('Starting items:')[1].split(',')
                self.items = [int(item) for item in items]
            elif line.strip().startswith('Operation'):
                items = line.split()
                self._operation_left = 'old' if items[3] == 'old' else int(items[3])
                self._operation_action = items[4]
                self._operation_right = 'old' if items[5] == 'old' else int(items[5])
            elif line.strip().startswith('Test'):
                items = line.split()
                self.test_divisible_by = int(items[3])
            elif line.strip().startswith('If true'):
                items = line.split()
                self.test_true_target = int(items[-1])
            elif line.strip().startswith('If false'):
                items = line.split()
                self.test_false_target = int(items[-1])
        self.inspection_count = 0
        


    def operation(self, value):
        self.inspection_count += 1
        left = value
        right = value if self._operation_right == 'old' else self._operation_right
        if self._operation_action == '+':
            result = left + right
        elif self._operation_action == '-':
            result = left - right
        elif self._operation_action == '*':
            result = left * right
        elif self._operation_action == '/':
            result = left / right
        else:
            raise NotImplementedError(f'OMG - action is not defined {self._operation_action}')
        return result % 9699690


    def test(self, value):
        if value % self.test_divisible_by == 0:
            return self.test_true_target
        else:
            return self.test_false_target

    def print_items(self):
        print(f'Monkey {self.num}: {self.items}')   

    def print_inspection_count(self):
        print(f'Monkey {self.num}: {self.inspection_count}')   


def run_round():
    for monkey in monkeys:
        for i, item in enumerate(monkey.items):
            monkey.items[i] = monkey.operation(item)
            monkeys[monkey.test(monkey.items[i])].items.append(monkey.items[i])
        monkey.items = []


with open('./day_11/input.txt') as f:
    data = f.read().split('\n\n')

monkeys = [Monkey(monkey) for monkey in data]

m1_counts = []
for _ in range(10000):
    run_round()
    m1_counts.append(monkeys[0].inspection_count)


print(f'm1 counts: {m1_counts}')
m1_deltas = [m1_counts[i] - m1_counts[i-1] for i in range(1, len(m1_counts))]
print(f'm1 deltas: {m1_deltas}')

print('inspection counts')
for monkey in monkeys:
    monkey.print_inspection_count()

# 5204 + 11


inspection_counts = sorted([monkey.inspection_count for monkey in monkeys])
monkey_business = inspection_counts[-1] * inspection_counts[-2]
print(f"monkey business: {monkey_business}")