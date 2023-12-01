
data = []
scores = []
def v(lst):
    count = 0
    for i in lst:
        count +=1
        if i:
            break
    return count


with open("day8/day8.txt") as f:
    for line in f:
        data.append(line.strip())

    for i in range(len(data)):
        for j in range(len(data[i])):
            current = data[i][j]
            side1 = v([current <= data[k][j] for k in range(i+1, len(data))]) # down
            side2 = v([current <= data[i][k] for k in range(j+1, len(data[i]))]) # right
            side3 = v([current <= data[k][j] for k in range(i-1, -1, -1)]) # up
            side4 = v([current <= data[i][k] for k in range(j-1, -1, -1)]) # left
            score = side1 * side2 * side3 * side4 
            scores.append(score)
            


print(max(scores))

