def genList(str):
    stack = []
    l = None
    i = 0
    while i < len(str):
        c = str[i]
        if c == '[':
            newList = []
            if len(stack) > 0:
                stack[-1].append(newList)
            stack.append(newList)
            
        elif c == ']':
            l = stack.pop(-1)
        elif c != ',':
            j = i
            while str[i] not in "[],":
                i+=1
            stack[-1].append(int(str[j:i]))
        i += 1
    print(l)
    return l

def solve():
    f = open("advent13.txt", 'r') 

    numInOrder = 0
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        l1 = genList(f.readline()[:-1])
        l2 = genList(f.readline()[:-1])
        break

    return numInOrder

print(solve())