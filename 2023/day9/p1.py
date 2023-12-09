with open("in.txt", "r") as f:
    numbers_list = [list(map(int, line.split())) for line in f.read().splitlines()]
    ans = 0

    for numbers in numbers_list:
        differences = [numbers]
        
        while not all(x == 0 for x in differences[-1]):
            new_diff = [differences[-1][i+1] - differences[-1][i] for i in range(len(differences[-1]) - 1)]
            differences.append(new_diff)

        for i in range(len(differences) - 1, 0, -1):
            last_value = differences[i][-1] + differences[i - 1][-1]
            differences[i - 1][-1] = last_value

        ans += last_value

    print(ans)
