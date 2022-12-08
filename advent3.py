def solve():
    f = open("advent3.txt", 'r')
    eof = False
    sumPriorities = 0
    while not eof:
        line1 = f.readline()
        line2 = f.readline()
        line3 = f.readline()
        if len(line1) <= 1:
            eof = True
        else:
            s1 = line1[:len(line1)]
            s2 = line2[:len(line2)]
            s3 = line3[:len(line3)]
            for c in s1:
                if c in s2 and c in s3:
                    if c.isupper():
                        sumPriorities += ord(c) - ord('A') + 27
                    else:
                        sumPriorities += ord(c) - ord('a') + 1
                    break
    return sumPriorities


print(solve())
