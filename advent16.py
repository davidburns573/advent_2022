from queue import PriorityQueue

def optimize(g):
    # gRev = dict()
    # for key in g:
    #     for edge in g[key][0]:
    #         if edge in gRev:
    #             gRev[edge].append(key)
    #         else:
    #             gRev[edge] = [key, 1]

    # keys = list(g.keys())
    # print(keys)
    # for key in keys:
    #     if g[key][1] == 0 and key != "AA":
    #         pipe = g[key]
    #         for fr in gRev[key]:
    #             for to in pipe[0]:
    #                 if to != fr and to not in g[fr][0]:
    #                     g[fr][0][to] = 1 + pipe[0][to]
    #                 elif to != fr:
    #                     g[fr][0][to] = min(1+pipe[0][to], g[fr][0][to])
    #             g[fr][0].pop(key)
    #         for fr in g[key]:
    #             for to in gRev[key]:
    #                 if to != fr and to not in g[fr][0]:
    #                     gRev[fr][0][to] = 1 + pipe[0][to]
    #                 elif to != fr:
    #                     gRev[fr][0][to] = min(1+pipe[0][to], g[fr][0][to])
    #         g.pop(key)
    bfs(g)
    keysToRemove = set()
    keys = list(g.keys())
    for key in keys:
        if g[key][1] == 0 and key != 'AA':
            keysToRemove.add(key)
            g.pop(key)
    for key in g:
        edges = list(g[key][0].keys())
        for edge in edges:
            if edge in keysToRemove or edge == key:
                g[key][0].pop(edge)

def bfs(g):
    for key in g:
        queue = PriorityQueue()
        visited = set()
        queue.put((0, key))
        while queue.qsize() > 0:
            curr = queue.get()
            if curr[1] in visited:
                continue
            visited.add(curr[1])
            if curr[1] != key and curr[1] not in g[key][0]:
                g[key][0][curr[1]] = curr[0]
            elif curr[1] != key:
                g[key][0][curr[1]] = min(g[key][0][curr[1]], curr[0])
            for edge in g[curr[1]][0]:
                queue.put((curr[0] + g[curr[1]][0][edge], edge))

def recurse(g, time, curr, total, path, possiblePaths, extraPath):
    if time <= 0 or total == 0:
        return 0
    gain = 0
    if curr != "AA":
        time -= 1
        gain = g[curr][1] * time
    future = 0
    for edge in g[curr][0]:
        if edge not in path and edge not in extraPath:
            path.append(edge)
            s = ' '.join(path)
            if len(extraPath) == 0:
                possiblePaths.add(s)
            res = recurse(g, time-g[curr][0][edge], edge, total - 1, path, possiblePaths, extraPath)
            future = max(future, res)
            path.pop(-1)
    return gain + future

def runPath(g, path, time):
    res = 0
    prev = "AA"
    for curr in path:
        if curr != "AA":
            time -= (g[prev][0][curr] + 1)
            res += g[curr][1] * time
            prev = curr
    return res

# DD -> BB -> JJ -> HH -> EE -> CC

def solve():
    f = open("advent16.txt", 'r')
    
    g = dict()
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        
        name = line[6:8]
        rate = int(line.split("=")[1].split(";")[0])
        edgesDict = dict()
        edges = line.split(";")[1].replace(" tunnels lead to valves ", "")[:-1].split(", ")
        if line.find(",") == -1:
            edges = [line.split(";")[1].replace(" tunnel leads to valve ", "")[:-1]]
        for e in edges:
            edgesDict[e] = 1
        g[name] = [edgesDict, rate]
    optimize(g)
    allPaths = set()
    recurse(g, 26, "AA", len(g), ["AA"], allPaths, [])
    best = 0
    count = 0
    allPathsSorted = dict()
    for path in allPaths:
        pathL = path.split(" ")
        pathL.sort()
        spath = ' '.join(pathL)
        res = runPath(g, path.split(" "), 26)
        if spath in allPathsSorted:
            if allPathsSorted[spath][1] < res:
                allPathsSorted[spath] = [path.split(" "), res]
        else:
            allPathsSorted[spath] = [path.split(" "), res]
    print(len(allPathsSorted))
    for path in allPathsSorted:
        pathL = allPathsSorted[path][0]
        if count % 100 == 0:
            print(count / 100, len(allPathsSorted)/100)
        best = max(best, allPathsSorted[path][1] + recurse(g, 26, "AA", len(g), ["AA"], allPaths, pathL))
        count += 1
    return best

print(solve())

