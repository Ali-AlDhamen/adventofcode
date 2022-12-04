def day3(part):

    total = 0
    count = 0
    temp_list = []
    
    with open('day3.txt') as f:
        lines = f.readlines()
        for line in lines:
            if part == 1:
                first_part = line[:int(len(line)/2)]
                second_part = line[int(len(line)/2):]
                for i in first_part:
                    if i in second_part:
                        if i.isupper():
                            total += ord(i) - 38
                            break
                        else:
                            total += ord(i) - 96
                            break

            else:
                count += 1
                temp_list.append(line)
                if count == 3:
                    count = 0
                    temp_list = sorted(temp_list, key=len)
                    for i in temp_list[2]:
                        if i in temp_list[0] and i in temp_list[1]:
                            if i.isupper():
                                total += ord(i) - 38
                                break
                            else:
                                total += ord(i) - 96
                                break
                    temp_list = []
    print(total)


day3(1)
day3(2)
