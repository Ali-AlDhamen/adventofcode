
x = 1
needs = [20, 60, 100, 140, 180, 220]
counter = 0
cycles = dict()
with open("day10/day10.txt") as f:
    for line in f:
        line = line.strip()

        if line == "noop":
            counter +=1
            cycles[counter] = x

        else:
            counter+=1
            cycles[counter] = x
            counter+=1
            cycles[counter] = x
            x += int(line.split(" ")[1])

ans = 0
for counter , value in cycles.items():
    if counter in needs:
        ans += value*counter

print(ans)

