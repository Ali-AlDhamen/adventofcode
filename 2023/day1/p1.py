with open("in.txt", 'r') as f:
    data = f.read().splitlines()
    ans = 0
    for line in data:
        temp = []
        for ch in line:
            if ch.isnumeric():
                temp.append(ch)   
        ans += int(temp[0] + temp[-1])
    print(ans)
