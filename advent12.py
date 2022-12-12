def bfs(grid, start):
    visited = [list([0 for i in range(len(grid[0]))]) for j in range(len(grid))]
    grid[start[0]][start[1]] = -1
    queue = [(start[0], start[1], 0)]
    while len(queue) > 0:
        s = queue.pop(0)
        if grid[s[0]][s[1]] == 0:
            return s[2]
        if visited[s[0]][s[1]] == 0:
            visited[s[0]][s[1]] = s[2]
            for i, j in [(1, 0), (0,1), (-1,0), (0,-1)]:
                x = s[0] + i
                y = s[1] + j
                if x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0]) \
                    and grid[x][y] >= grid[s[0]][s[1]] - 1:
                    queue.append((x,y,s[2]+1))


def solve():
    f = open("advent12.txt", "r")
    
    grid = []
    start = None
    end = None
    rowNum = 0
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        row = [(ord(i)-ord('a')) for i in line[:-1]]
        grid.append(row)
        for i, c in enumerate(line):
            if c == 'S':
                start = (rowNum, i)
            if c == 'E':
                end = (rowNum, i)
        rowNum += 1

    return bfs(grid, end)

print(solve())