def solve():
    f = open("advent11.txt", 'r')

    monkeys = []
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        line = f.readline()
        line = line.replace("  Starting items: ", "")[:-1]
        items = [int(i) for i in line.split(", ")]
        line = f.readline().replace("  Operation: new = ", "")
        line = line.replace("old", 'x')[:-1]
        op = lambda x: x * x
        if line[4] != 'x':
            num = int(line[4:])
            if line[2] == '*':
                op = lambda x: x * num
            elif line[2] == '+':
                op = lambda x: x + num
        line = f.readline().replace("  Test: divisible by ", "")[:-1]
        num = int(line)
        test = lambda x: x % num == 0
        monkeyT = int(f.readline().replace("    If true: throw to monkey ", "")[:-1])
        monkeyF = int(f.readline().replace("    If false: throw to monkey ", "")[:-1])
        f.readline()

        monkeys.append(Monkey(items, op, test, monkeyT, monkeyF))

    for monkey in monkeys:
        monkey.updatePassMonkeys(monkeys[monkey.monkeyT], monkeys[monkey.monkeyF])
    
    for i in range(20):
        for monkey in monkeys:
            monkey.simulate()
    
    monkeys.sort(key=lambda x: x.numPasses)
    for m in monkeys:
        print(m.numPasses)
    return monkeys[-1].numPasses * monkeys[-2].numPasses
    


class Monkey:
    def __init__(self, items, operation, test, monkeyT, monkeyF):
        self.items = items
        self.operation = operation
        self.test = test
        self.monkeyT = monkeyT
        self.monkeyF = monkeyF
        self.numPasses = 0
    
    def updatePassMonkeys(self, monkeyT, monkeyF):
        self.monkeyT = monkeyT
        self.monkeyF = monkeyF
    
    def simulate(self):
        while len(self.items) > 0:
            self.numPasses += 1
            item = self.items.pop(0)
            cost = int(self.operation(item) / 3)
            if self.test(cost):
                self.monkeyT.items.append(cost)
            else:
                self.monkeyF.items.append(cost)

print(solve())