with open("in.txt", 'r') as f:
    data = f.read().splitlines()
    ans = 0
    for case in data:
        case = ''.join(case.split(":")[1:]).strip().split("|")
        winning_cards = [int(x) for x in case[0].split(" ") if x]
        my_cards = [int(x) for x in case[1].split(" ") if x and int(x) in winning_cards]
        if my_cards:
            ans += pow(2, len(my_cards)-1)
    print(ans)
    