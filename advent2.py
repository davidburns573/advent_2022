def solve():
    f = open("./advent2.txt", "r")
    
    isEmpty = False
    totalScore = 0
    while not isEmpty:
        line = f.readline()
        if len(line) == 0:
            isEmpty = True
        else:
            p = ord(line[0]) - ord('A') + 1
            y = ord(line[2]) - ord('X')
            totalScore += y * 3
            
            if y == 0:
                if p == 1:
                    totalScore += 3
                elif p == 2:
                    totalScore += 1
                else:
                    totalScore += 2
            elif y == 1:
                totalScore += p
            else:
                if p == 1:
                    totalScore += 2
                elif p == 2:
                    totalScore += 3
                else:
                    totalScore += 1
    return totalScore

print(solve())

    