with open("in.txt", 'r') as f:
     data = f.read().splitlines()
     left = []
     right = []
     for line in data:
         a, b = line.split("  ")
         left.append(int(a))
         right.append(int(b))
     total = 0
     for i in range(len(left)):
         total += left[i] * right.count(left[i])
     print(total)
         
     