def extract_number_and_end_index(line, index):
    number = ""
    i = index
    while i < len(line) and line[i].isdigit():
        number += line[i]
        i += 1
    end_index = i
    i = index-1
    while i >= 0 and line[i].isdigit():
        number = line[i] + number
        i -= 1
    return int(number)


def find_numbers(data,row,col):
    numbers = set()
    if (row-1) >= 0 and data[row-1][col].isdigit():
        numbers.add(extract_number_and_end_index(data[row-1], col))
    if (row+1) < len(data) and data[row+1][col].isdigit():
        numbers.add(extract_number_and_end_index(data[row+1], col))
    if (col+1) < len(data[row]) and data[row][col+1].isdigit():
        numbers.add(extract_number_and_end_index(data[row], col+1))
    if (col-1) >= 0 and data[row][col-1].isdigit():
        numbers.add(extract_number_and_end_index(data[row], col-1))
    if (row-1) >= 0 and (col+1) < len(data[row-1]) and data[row-1][col+1].isdigit():
        numbers.add(extract_number_and_end_index(data[row-1], col+1))
    if (row-1) >= 0 and (col-1) >= 0 and data[row-1][col-1].isdigit():
        numbers.add(extract_number_and_end_index(data[row-1], col-1))
    if (row+1) < len(data) and (col+1) < len(data[row]) and data[row+1][col+1].isdigit():
        numbers.add(extract_number_and_end_index(data[row+1], col+1))
    if (row+1) < len(data) and (col-1) >= 0 and data[row+1][col-1].isdigit():
        numbers.add(extract_number_and_end_index(data[row+1], col-1))
    
    if len(numbers) == 2:
        nums = list(numbers)
        return nums[0] * nums[1]
    return False
    

with open("in.txt", 'r') as f:
    data = f.read().splitlines()
    ans = 0
    for i, line in enumerate(data):
        for j, ch in enumerate(line):
            if ch == '*': 
                res = find_numbers(data, i, j)
                if res is not False:
                    ans += res
    print(ans)