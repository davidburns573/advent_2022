def findPath(dir, path):
    if path == '/':
        return dir
    dirs = path.split('/')
    dirs = dirs[1:]
    dirPtr = dir
    init = True
    for d in dirs:
        if init:
            dirPtr = dirPtr[d][1]
        else:
            dirPtr = dirPtr[1][d][1]
    return dirPtr

def handleLs(f, dir):
    endOfCommand = False
    while not endOfCommand:
        resetLine = f.tell()
        line = f.readline()
        if len(line) > 0 and line[0] != '$':
            parts = line.split(" ")
            parts[1] = parts[1][:-1]
            if parts[0] == "dir":
                dir[parts[1]] = ('d', dict())
            else:
                dir[parts[1]] = ('f', int(parts[0]))
        else:
            endOfCommand = True
            f.seek(resetLine)

def handleCd(path, com):
    if com == "..":
        return '/'.join(path.split("/")[:-1])
    else:
        if path == "/":
            return path + com
        else:
            return path + "/" + com

def dfs(dir, dirSizes):
    currSum = 0
    for key in dir:
        tup = dir[key]
        if tup[0] == 'd':
            currSum += dfs(tup[1], dirSizes)
        else:
            currSum += tup[1]
    dirSizes.append(currSum)
    return currSum

def solve():
    f = open("advent7.txt", 'r')
    dir = dict()
    path = '/'

    eof = False
    while not eof:
        line = f.readline()
        if len(line) == 0:
            eof = True
        else:
            if line[0:4] == "$ ls":
                nDir = findPath(dir, path)
                handleLs(f, nDir)
            elif line[0:4] == "$ cd":
                path = handleCd(path, line[5:-1])
    
    dirSizes = []
    total = dfs(dir, dirSizes)
    dirSizes.sort()
    toRemove = total - 40000000
    for dirSize in dirSizes:
        if dirSize >= toRemove:
            return dirSize

print(solve())