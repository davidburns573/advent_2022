def printGrid(grid):
    for i in range(len(grid)):
        for j in range(400,len(grid[0])):
            print(grid[i][j],end='')
        print("")

def simulate(grid):
    x, y = (0, 500)
    if grid[x][y] == 'o':
        return False
    while True:
        if x+1 >= len(grid):
            return False
        if grid[x+1][y] == '.':
            x += 1
            # print("t",end='')
        elif grid[x+1][y-1] == '.':
            y -= 1
            x += 1
        elif grid[x+1][y+1] == '.':
            y += 1
            x += 1
        else:
            grid[x][y] = 'o'
            return True

def solve():
    f = open("advent14.txt", "r")

    grid = [list(['.' for j in range(1000)]) for i in range(350)]

    mx = 0
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        nums = [(int(y[0]), int(y[1])) for y in [x.split(",") for x in line.split(" -> ")]]
        p = None
        for y,x in nums:
            if p != None:
                py, px = p
                while px != x or py != y:
                    grid[px][py] = '#'
                    px += int((x - px)/abs(x - px)) if px != x else 0
                    py += int((y - py)/abs(y - py)) if py != y else 0
                grid[x][y] = '#'
            p = (y,x)
            mx = max(x, mx)

    for i in range(len(grid[0])):
        grid[2+mx][i] = "#"

    while True:
        if not simulate(grid):
            break
    printGrid(grid)

    s = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'o':
                s += 1
    return s

print(solve())