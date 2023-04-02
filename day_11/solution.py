import time
start_time = time.time()

with open('input.txt') as f:
    data = f.read().split('\n\n')

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
            raise NotImplementedError(f'action is not defined {self._operation_action}')
        return result 

    def test(self, value):
        if value % self.test_divisible_by == 0:
            return self.test_true_target
        else:
            return self.test_false_target


def run_rounds(num_rounds, worry_level):
    monkies = [Monkey(monkey) for monkey in data]
    mult = worry_level
    for m in monkies:
        mult *= m.test_divisible_by
    for _ in range(num_rounds):
        for monkey in monkies:
            for i, item in enumerate(monkey.items):
                monkey.items[i] = monkey.operation(item) % mult
                monkies[monkey.test(monkey.items[i]//worry_level)].items.append(monkey.items[i]//worry_level)
            monkey.items = []
    inspection_counts = sorted([monkey.inspection_count for monkey in monkies])
    return inspection_counts[-1] * inspection_counts[-2]


print(f"Part 1 answer: {run_rounds(20, 3)}")
print(f"Part 2 answer: {run_rounds(10000, 1)}")
elapsed = time.time() - start_time
end_time = time.time()
print(f"Time: {round((elapsed)*1000, 4)}ms")