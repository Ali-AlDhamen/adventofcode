def extract_number_and_end_index(line, index):
    number = ""
    i = index
    end_index = index
    while i < len(line) and line[i].isdigit():
        number += line[i]
        i += 1
    end_index = i
    i = index-1
    while i >= 0 and line[i].isdigit():
        number = line[i] + number
        i -= 1
    return int(number) , end_index


def find_symbols(data,row,col):
    
    if (row-1) >= 0 and not data[row-1][col].isdigit() and data[row-1][col] != ".":
        return True

    if (row+1) < len(data) and not data[row+1][col].isdigit() and data[row+1][col] != ".":
        return True
    
    if (col+1) < len(data[row]) and not data[row][col+1].isdigit() and data[row][col+1] != ".":
        return True
    
    if (col-1) >= 0 and not data[row][col-1].isdigit() and data[row][col-1] != ".":
        return True
    
    if (row-1) >= 0 and (col+1) < len(data[row-1]) and not data[row-1][col+1].isdigit() and data[row-1][col+1] != ".":
        return True
    
    if (row-1) >= 0 and (col-1) >= 0 and not data[row-1][col-1].isdigit() and data[row-1][col-1] != ".":
        return True
    
    if (row+1) < len(data) and (col+1) < len(data[row]) and not data[row+1][col+1].isdigit() and data[row+1][col+1] != ".":
        return True
    
    if (row+1) < len(data) and (col-1) >= 0 and not data[row+1][col-1].isdigit() and data[row+1][col-1] != ".":
        return True
    return False

    
    

with open("in.txt", 'r') as f:
    data = f.read().splitlines()
    ans = 0
    for i, line in enumerate(data):
        end_index = 0 
        f = False
        for j, ch in enumerate(line):
            if f and j < end_index:
                continue
            if ch.isdigit(): 
                if find_symbols(data, i, j):
                    number , end_index = extract_number_and_end_index(line, j)
                    ans += number
                    f = True
    print(ans)