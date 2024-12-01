with open("in.txt", 'r') as f:
     data = f.read().splitlines()
     left = []
     right = []
     for line in data:
         a, b = line.split("  ")
         left.append(int(a))
         right.append(int(b))
     left = sorted(left)
     right = sorted(right)
     total = 0
     for i in range(len(left)):
         total += abs(left[i] - right[i])
     print(total)
         
     