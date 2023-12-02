with open("in.txt", 'r') as f:
    data = f.read().splitlines()
    maxRed = 12
    maxGreen = 13
    maxBlue = 14
    ans = 0
    for line in data:
        id = int(line.split(":")[0].split(" ")[1])
        line = ''.join(line.split(":")[1:])
        line = line.split(";")
        lines = list(map(lambda x: x.strip().split(", "), line))
        good = True
        for colors in lines:      
            for c in colors:
                amount , color = int(c.split(" ")[0]), c.split(" ")[1]
                if color == "red" and amount > maxRed:
                    good = False
                elif color == "green" and amount > maxGreen:
                    good = False
                elif color == "blue" and amount > maxBlue:
                    good = False
        if good:       
            ans += id
            

    print(ans)
    