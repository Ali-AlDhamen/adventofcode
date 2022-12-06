
# part 1
with open('day6/day6.txt') as f:
    line = f.readlines()
    line = line[0].strip()
    marker = ""
    for i in range(len(line)):
        marker += line[i]
        
        if len(marker) == 4 and len(set(marker)) == 4:
            print(i+1)
            break
        elif len(marker) == 4 and len(set(marker)) != 4:
            marker = marker[1:]
            


# part 2
with open('day6/day6.txt') as f:
    line = f.readlines()
    line = line[0].strip()
    marker = ""
    for i in range(len(line)):
        marker += line[i]
        
        if len(marker) == 14 and len(set(marker)) == 14:
            print(i+1)
            break
        elif len(marker) == 14 and len(set(marker)) != 14:
            marker = marker[1:]