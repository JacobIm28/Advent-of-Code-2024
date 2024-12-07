grid = []
with open('data.txt') as f:
  for line in f:
    grid.append(list(line.strip()))

guard = [] # [x, y, direction]

for i in range(len(grid)):
  for j in range(len(grid[i])):
    if grid[i][j] != "." and grid[i][j] != "#":
      guard = [i, j, 0]
      grid[i][j] == "."

def isOnBoard(r, c):
  return r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0])

print(guard)
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
visited = set()

while isOnBoard(guard[0], guard[1]):
  visited.add((guard[0], guard[1]))

  rr, cc = guard[0] + direction[guard[2]][0], guard[1] + direction[guard[2]][1]
  print(rr, cc)

  if not isOnBoard(rr, cc):
    break
  elif grid[rr][cc] == "#":
    guard[2] = (guard[2] + 1) % 4
  else:
    guard[0], guard[1] = rr, cc

print(len(visited))

