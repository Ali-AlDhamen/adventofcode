with open("in.txt", 'r') as f:
    data = f.read().splitlines()
    cards_count = {}
    ans = 0
    for case in data:
        case_number = int(case.split(":")[0].split(" ")[-1])
        case = ''.join(case.split(":")[1:]).strip().split("|")
        winning_cards = [int(x) for x in case[0].split(" ") if x]
        my_cards = [int(x) for x in case[1].split(" ") if x and int(x) in winning_cards]
        cards_count[case_number] = cards_count.get(case_number, 1)
        for i in range(case_number+1, len(my_cards)+case_number+1):
            cards_count[i] = cards_count.get(i, 1) + cards_count[case_number]
    print(sum(cards_count.values()))