

total = 0

with open('day4/day4.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        words = line.split(",")
        first_pair = tuple(words[0].split("-"))
        second_pair = tuple(words[1].split("-"))
        range2 = list(range(int(second_pair[0]) ,int(second_pair[1])+1))
        if int(first_pair[0]) <= int(second_pair[0]) and int(first_pair[1]) >= int(second_pair[1]):
            total +=1
        elif int(first_pair[0]) >= int(second_pair[0]) and int(first_pair[1]) <= int(second_pair[1]):
            total +=1
        # this else if for 2nd part
        elif int(first_pair[0]) in range2 or int(first_pair[1]) in range2:
            total +=1


print(total)


