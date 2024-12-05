grid = []

with open('data.txt') as f:
  for line in f:
    grid.append(list(line.strip()))

ROWS, COLS = len(grid), len(grid[0])

d = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

def isXmas(r, c):
  if r <= 0 or r >= ROWS - 1 or c <= 0 or c >= COLS - 1:
    return False
  else:
    diag1, diag2 = '', ''

    diag1 += grid[r - 1][c - 1] + grid[r + 1][c + 1]
    diag2 += grid[r - 1][c + 1] + grid[r + 1][c - 1]

    print(r, c, diag1, diag2)

    return 'M' in diag1 and 'S' in diag1 and 'M' in diag2 and 'S' in diag2

count = 0

for r in range(ROWS):
  for c in range(COLS):
    if grid[r][c] == 'A' and isXmas(r, c):
      count += 1

print(count)
    

