def solve():
    f = open("advent4.txt", 'r')
    eof = False
    total = 0
    while not eof:
        line = f.readline()
        if len(line) == 0:
            eof = True
        else:
            line = line[0:len(line)-1]
            strs = line.split(',')
            t1 = strs[0].split('-')
            t1 = (int(t1[0]), int(t1[1]))
            t2 = strs[1].split('-')
            t2 = (int(t2[0]), int(t2[1]))
            print(t1, t2)
            if (t1[0] <= t2[0] and t1[1] >= t2[0]) or (t1[0] <= t2[1] and t1[1] >= t2[1]) or (t1[0] >= t2[0] and t1[1] <= t2[1]):
                total += 1
    return total


print(solve())
