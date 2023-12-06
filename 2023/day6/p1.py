from functools import reduce

with open("in.txt", 'r') as f:
    time = [int(x) for x in f.readline().strip().split(" ")[1:] if x]
    distance = [int(x) for x in f.readline().strip().split(" ")[1:] if x]
    races = list(zip(time, distance))

    ans = []
    ways = 0
    
    for time, distance in races:
        for i in range(time):
            total_distance = i * (time-i)
            if total_distance > distance:
                ways += 1
        ans.append(ways)
        ways = 0
        
    ans = reduce(lambda x, y: x*y, ans)
    print(ans)
        