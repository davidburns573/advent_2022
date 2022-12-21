from functools import cmp_to_key

def genList(str):
    stack = []
    l = None
    i = 0
    while i < len(str):
        c = str[i]
        if c == '[':
            stack.append(list())
        elif c == ']':
            l = stack.pop(-1)
            if len(stack) > 0:
                stack[-1].append(l)
        elif c != ',':
            j = i
            while str[i] not in "[],":
                i+=1
            stack[-1].append(int(str[j:i]))
            i-=1
        i += 1
    return l

def step(l1, l2):
    i = 0
    while i < len(l1) and i < len(l2):
        c1 = l1[i]
        c2 = l2[i]
        r = 0
        if type(c1) is int and type(c2) is int:
            if c1 < c2:
                return -1
            elif c1 > c2:
                return 1
        elif type(c1) is int or type(c2) is int:
            r = step(c1, [c2]) if type(c2) is int else step([c1], c2)
        else:
            r = step(c1, c2)
        if r == -1 or r == 1:
            return r
        i += 1
    if len(l1) == i and len(l2) == i:
        return 0
    elif len(l1) == i:
        return -1
    else:
        return 1
        
def solve():
    f = open("advent13.txt", 'r') 

    allPairs = []
    pairs = None
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        l1 = genList(f.readline()[:-1])
        l2 = genList(f.readline()[:-1])
        if pairs is None:
            pairs = (l1, l2)
        allPairs.append(l1)
        allPairs.append(l2)
    allPairs.sort(key=cmp_to_key(step))
                    
    return (allPairs.index(pairs[0])+1) * (allPairs.index(pairs[1])+1)

print(solve())