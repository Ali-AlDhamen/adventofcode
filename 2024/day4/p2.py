with open("in.txt") as f:
    grid = f.read().strip().split('\n')

rows = len(grid)
cols = len(grid[0])
count = 0

for r in range(1, rows-1):
    for c in range(1, cols-1):
        if grid[r][c] != 'A':
            continue
            
        diag1 = grid[r-1][c-1] + grid[r+1][c+1]
        diag2 = grid[r-1][c+1] + grid[r+1][c-1]
        
        if (diag1 in ['MS','SM']) and (diag2 in ['MS','SM']):
            count += 1

print(count)