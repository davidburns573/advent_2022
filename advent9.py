def printMap(snake):
    for i in range(10, -10, -1):
        for j in range(-10, 10):
            p = False
            for k in range(len(snake)):
                if snake[k][0] == j and snake[k][1] == i:
                    print(k,end='')
                    p = True
                    break
            if not p:
                print(".",end='')
        print('')

def solve():
    f = open("advent9.txt", 'r')
    visited = set()
    visited.add((0,0))
    eof = False
    snake = []
    for i in range(10):
        snake.append([0,0])

    while not eof:
        line = f.readline()
        if len(line) == 0:
            eof = True
        else:
            d = line[0]
            x = int(line[2:-1])

            for i in range(x):
                if d == 'U':
                    snake[0][1] += 1
                elif d == 'D':
                    snake[0][1] -= 1
                elif d == 'L':
                    snake[0][0] -= 1
                elif d == 'R':
                    snake[0][0] += 1
                for j in range(1, len(snake)):
                    H = snake[j-1]
                    T = snake[j]
                    if abs(H[0] - T[0]) <= 1 and abs(H[1] - T[1]) <= 1:
                        continue
                    if abs(H[0] - T[0]) == 2 and abs(H[1] - T[1]) == 2:
                        snake[j][0] += int((H[0] - T[0]) / 2)
                        snake[j][1] += int((H[1] - T[1]) / 2)
                    elif abs(H[0] - T[0]) == 2:
                        snake[j][0] += int((H[0] - T[0]) / 2)
                        if abs(H[1] - T[1]) == 1:
                            snake[j][1] += H[1] - T[1]
                    elif abs(H[1] - T[1]) == 2:
                        snake[j][1] += int((H[1] - T[1]) / 2)
                        if abs(H[0] - T[0]) == 1:
                            snake[j][0] += H[0] - T[0]
                visited.add((snake[9][0], snake[9][1]))
    
    return len(visited)

    

print(solve())