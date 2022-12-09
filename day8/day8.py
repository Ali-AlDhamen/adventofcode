
data = []
show = 0

scores = []


def v(lst):
    return False not in lst


with open("day8/day8.txt") as f:
    for line in f:
        data.append(line.strip())

    for i in range(len(data)):
        for j in range(len(data[i])):
            current = data[i][j]
            if i == 0 or i == len(data) - 1 or j == 0 or j == len(data) - 1:
                show += 1
                continue
            elif v([current > data[k][j] for k in range(i+1, len(data))]) or v([current > data[i][k] for k in range(j+1, len(data[i]))]) or v([current > data[k][j] for k in range(i-1, -1, -1)]) or v([current > data[i][k] for k in range(j-1, -1, -1)]):
                show += 1


print(show)
