def solve():
    f = open("advent8.txt", 'r')

    grid = []
    seen = []
    eof = False
    while not eof:
        line = f.readline()
        if len(line) == 0:
            eof = True
        else:
            grid.append([])
            seen.append([])
            for t in line[:-1]:
                grid[-1].append(int(t))
                seen[-1].append(0)

    bestScore = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            countU = 0
            for k in range(i-1, -1, -1):
                countU += 1
                if grid[k][j] >= grid[i][j]:
                    break
            countD = 0
            for k in range(i+1, len(grid)):
                countD += 1
                if grid[k][j] >= grid[i][j]:
                    break
            countL = 0
            for k in range(j-1, -1, -1):
                countL += 1
                if grid[i][k] >= grid[i][j]:
                    break
            countR = 0
            for k in range(j+1, len(grid[0])):
                countR += 1
                if grid[i][k] >= grid[i][j]:
                    break
            bestScore = max(bestScore, countU*countD*countR*countL)
    return bestScore

    # for i in range(0, len(grid[0])):
    #     m = -1
    #     for j in range(0, len(grid)):
    #         if grid[j][i] > m:
    #             seen[j][i] = 1
    #             m = grid[j][i]
    # for i in range(len(grid[0])):
    #     m = -1
    #     for j in range(len(grid)-1, -1, -1):
    #         if grid[j][i] > m:
    #             seen[j][i] = 1
    #             m = grid[j][i]
    # for i in range(len(grid)):
    #     m = -1
    #     for j in range(len(grid[0])):
    #         if grid[i][j] > m:
    #             seen[i][j] = 1
    #             m = grid[i][j]
    # for i in range(len(grid)):
    #     m = -1
    #     for j in range(len(grid[0])-1,-1,-1):
    #         if grid[i][j] > m:
    #             seen[i][j] = 1
    #             m = grid[i][j]

    # countVis = 0
    # for row in seen:
    #     for i in row:
    #         if i == 1:
    #             countVis += 1
    # return countVis

print(solve())