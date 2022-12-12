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
        num = 'x'
        op = line[2]
        if line[4] != 'x':
            num = int(line[4:])
        line = f.readline().replace("  Test: divisible by ", "")[:-1]
        test = int(line)
        monkeyT = int(f.readline().replace("    If true: throw to monkey ", "")[:-1])
        monkeyF = int(f.readline().replace("    If false: throw to monkey ", "")[:-1])
        f.readline()

        monkeys.append(Monkey(items, op, num, test, monkeyT, monkeyF))

    divisible = 1
    for monkey in monkeys:
        divisible *= monkey.test
        monkey.updatePassMonkeys(monkeys[monkey.monkeyT], monkeys[monkey.monkeyF])
    print(divisible)
    
    for i in range(10000):
        if i % 1000 == 0:
            print(i)
        for monkey in monkeys:
            monkey.simulate()
    
    monkeys.sort(key=lambda x: x.numPasses)
    return monkeys[-1].numPasses * monkeys[-2].numPasses
    


class Monkey:
    def __init__(self, items, operation, num, test, monkeyT, monkeyF):
        self.items = items
        self.operation = operation
        self.test = test
        self.num = num
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
            cost = item * item
            if self.num != 'x': 
                if self.operation == '*':
                    cost = self.num * item
                else:
                    cost = self.num + item
            if (cost % self.test) == 0:
                self.monkeyT.items.append((cost % 9699690))
            else:
                self.monkeyF.items.append(cost)

print(solve())