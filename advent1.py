def solve():
    f = open("./advent1.txt", "r")
    fileEmpty = False
    runningSum = 0
    l = []
    while not fileEmpty:
        line = f.readline()
        if len(line) > 1:
            runningSum += int(line)
        elif len(line) == 1:
            if len(l) < 3:
                l.append(runningSum)
                l.sort()
            elif runningSum >= l[0]:
                l[0] = runningSum
                l.sort()
            runningSum = 0
        else:
            fileEmpty = True
    return sum(l)
        
print(solve())