x = 1
counter = -1
cycles = dict()
with open("day10/day10.txt") as f:
    for line in f:
        line = line.strip()

        if line == "noop":
            counter += 1
            cycles[counter] = x

        else:
            counter += 1
            cycles[counter] = x
            counter += 1
            cycles[counter] = x
            x += int(line.split(" ")[1])

for i, j in cycles.items():
    if i % 40 == 0:
        for k in range(40):
            if abs(cycles[i+k] - k) <= 1:
                print("#", end="")
            else:
                print(".", end="")
        print()