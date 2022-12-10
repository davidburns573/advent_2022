def printScreen(screen):
    for i in range(6):
        for j in range(40):
            print(screen[i][j], end='')
        print("")


def solve():
    f = open("advent10.txt", 'r')

    screen = [list(['.' for j in range(40)]) for i in range(6)]

    currCycle = 1
    reg = 1
    eof = False
    while not eof:
        line = f.readline()
        if len(line) == 0:
            eof = True
        else:
            pixel = (int(currCycle / 40), currCycle % 40)
            if pixel[1] >= reg and pixel[1] < reg + 3:
                screen[pixel[0]][pixel[1]] = '#'
            if currCycle % 240 == 0:
                printScreen(screen)
                screen = [list(['.' for j in range(40)]) for i in range(6)]
            if line[0] == 'n':
                currCycle += 1
            else:
                num = int(line[5:-1])
                currCycle += 1
                pixel = (int(currCycle / 40), currCycle % 40)
                if pixel[1] >= reg and pixel[1] < reg + 3:
                    screen[pixel[0]][pixel[1]] = '#'
                if currCycle % 240 == 0:
                    printScreen(screen)
                    screen = [list(['.' for j in range(40)]) for i in range(6)]
                currCycle += 1
                reg += num


print(solve())
