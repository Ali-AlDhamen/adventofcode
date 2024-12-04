with open("in.txt") as f:
    grid = f.read().strip().split('\n')

rows = len(grid)
cols = len(grid[0])
count = 0
dirs = [(i,j) for i in (-1,0,1) for j in (-1,0,1) if i != 0 or j != 0]
target = "XMAS"
for r in range(rows):
    for c in range(cols):
        for dx,dy in dirs:
            ok = True
            for k in range(4):
                nr = r + k*dx
                nc = c + k*dy
                if not (0 <= nr < rows and 0 <= nc < cols):
                    ok = False
                    break
                if grid[nr][nc] != target[k]:
                    ok = False
                    break
            count += 1 if ok else 0
            
print(count)