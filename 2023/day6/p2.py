with open("in.txt", 'r') as f:
    time = int(''.join( [x for x in f.readline().strip().split(" ")[1:] if x]))
    distance = int(''.join([x for x in f.readline().strip().split(" ")[1:] if x]))
    ways = 0
    for i in range(time):
            total_distance = i * (time-i)
            if total_distance > distance:
                ways += 1
    print(ways)
        