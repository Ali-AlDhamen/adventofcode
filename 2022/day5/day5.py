# [C]         [S] [H]
# [F] [B]     [C] [S]     [W]
# [B] [W]     [W] [M] [S] [B]
# [L] [H] [G] [L] [P] [F] [Q]
# [D] [P] [J] [F] [T] [G] [M] [T]
# [P] [G] [B] [N] [L] [W] [P] [W] [R]
# [Z] [V] [W] [J] [J] [C] [T] [S] [C]
# [S] [N] [F] [G] [W] [B] [H] [F] [N]


lst = [
    ['C', 'F', 'B', 'L', 'D', 'P', 'Z', 'S'], ['B', 'W', 'H', 'P', 'G', 'V', 'N'], ['G', 'J', 'B', 'W', 'F'], ['S', 'C', 'W', 'L', 'F', 'N', 'J', 'G'], [
        'H', 'S', 'M', 'P', 'T', 'L', 'J', 'W'], ['S', 'F', 'G', 'W', 'C', 'B'], ['W', 'B', 'Q', 'M', 'P', 'T', 'H'], ['T', 'W', 'S', 'F'], ['R', 'C', 'N']
]

for i in lst:
    i.reverse()

result = ""
with open('day5/day5.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip().split(' ')
        creates_numbers = int(line[1])
        from_create = int(line[3])-1
        to_create = int(line[5])-1
        temp = lst[from_create][-creates_numbers:]
        temp.reverse()  # for part 2 just remove this line
        lst[from_create] = lst[from_create][:-creates_numbers]
        lst[to_create] = lst[to_create] + temp
        temp.clear()


for i in lst:
    result += i[-1]

print(result)
