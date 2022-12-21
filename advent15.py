from queue import PriorityQueue

def solve():
    f = open("advent15.txt", "r")
    
    areas = []
    data = []
    while True:
        line = f.readline()
        if len(line) == 0:
            break

        line = line.replace("Sensor at x=", "")
        line = line.replace(" closest beacon is at x=","")
        line = line.replace(" y=","")[:-1]
        sensor = [int(x) for x in line.split(":")[0].split(",")]
        beacon = [int(x) for x in line.split(":")[1].split(",")]
        data.append((sensor, beacon))

    def find(data, yval):
        bounds = []
        for d in data:
            sensor, beacon = d
            dist = abs(sensor[0]-beacon[0]) + abs(sensor[1]-beacon[1])
            areas.append((sensor[0], sensor[1], dist))
            rem = dist - abs(sensor[1] - yval)
            if rem >= 0:
                bounds.append([sensor[0] - rem, sensor[0] + rem])

        bounds.sort(key=lambda x: x[0])
        i = 1
        while i < len(bounds):
            if bounds[i][0] <= bounds[i-1][1]:
                bounds[i-1][1] = max(bounds[i][1], bounds[i-1][1])
                bounds.pop(i)
            else:
                i += 1
        s = 0
        for bound in bounds:
            s += bound[1] - bound[0]
        if len(bounds) > 1:
            print((bounds[0][1] + 1) * 4000000 + yval)
            print(bounds)
        elif bounds[0][0] >= 0 or bounds[0][1] <= 4000000:
            print(bounds)
    
    for yval in range(4000001):
        if yval % 40000 == 0:
            print(yval / 40000, 100)
        find(data, yval)

    return None

print(solve())