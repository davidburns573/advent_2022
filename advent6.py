def solve():
    f = open("advent6.txt", 'r')
    str = f.readline()
    
    for i in range(14, len(str)):
        valid = True
        for j in range(i-14, i):
            if str[j] in str[j+1:i]:
                valid = False
        if valid:
            return i

print(solve())