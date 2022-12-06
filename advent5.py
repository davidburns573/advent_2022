def solve():
    f = open("advent5.txt", 'r')

    stacks = [list() for i in range(9)]
    for i in range(8):
        line = f.readline()
        index = 1
        for j in range(9):
            if line[index] != ' ':
                stacks[j].insert(0, line[index])
            index += 4

    f.readline()
    f.readline()
    
    eof = False
    while not eof:
        line = f.readline()
        if len(line) == 0:
            eof = True
        else:
            moves = [int(i) for i in line.split() if i not in ["move", "from", "to"]]
            count, fr, to = moves
            fr-=1
            to-=1
            temp = stacks[fr][-count:]
            stacks[fr] = stacks[fr][:-count]
            stacks[to] += temp

    res = ""
    for stack in stacks:
        if len(stack) == 0:
            res += ' '
        else:
            res += stack[-1]
    return res

print(solve())