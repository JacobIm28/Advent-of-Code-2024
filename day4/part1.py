grid = []

with open('data.txt') as f:
  for line in f:
    grid.append(list(line.strip()))

ROWS, COLS = len(grid), len(grid[0])

d = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

def searchWord(r, c):
  possible = [''] * 8

  for x in range(4):
    for i, offset in enumerate(d):
      di, dj = offset
      ii, jj = r + x * di, c + x * dj

      if ii < 0 or ii >= ROWS or jj < 0 or jj >= COLS:
        continue
      else:
        possible[i] += grid[ii][jj]
  print(possible)
  return len([w for w in possible if w == 'XMAS'])

count = 0

for r in range(ROWS):
  for c in range(COLS):
    if grid[r][c] == 'X':
      print(r, c, searchWord(r, c))
      count += searchWord(r, c)

print(count)
    

