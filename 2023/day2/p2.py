with open("in.txt", 'r') as f:
    data = f.read().splitlines()
    ans = 0
    for line in data:
        maxRed = 1
        maxGreen = 1
        maxBlue = 1
        id = int(line.split(":")[0].split(" ")[1])
        line = ''.join(line.split(":")[1:])
        line = line.split(";")
        lines = list(map(lambda x: x.strip().split(", "), line))
        for colors in lines:      
            for c in colors:
                amount , color = int(c.split(" ")[0]), c.split(" ")[1]
                if color == "red":
                    maxRed = max(maxRed, amount)
                elif color == "green":
                    maxGreen = max(maxGreen, amount)
                elif color == "blue":
                    maxBlue = max(maxBlue, amount)
        ans +=  maxRed * maxGreen * maxBlue
            

    print(ans)
    