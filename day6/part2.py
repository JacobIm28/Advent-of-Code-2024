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

def isLoop():
  print("in is looop", guard)

  turn_points = set()

  while True:
    if canMove():
      rr, cc = guard[0] + direction[guard[2]][0], guard[1] + direction[guard[2]][1]
      guard[0], guard[1] = rr, cc
    elif not isOnBoard(guard[0] + direction[guard[2]][0], guard[1] + direction[guard[2]][1]):
      break
    else:
      if tuple(guard) in turn_points:
        return True
      turn_points.add(tuple(guard))
      guard[2] = (guard[2] + 1) % 4

  return False

def canMove():
  rr, cc = guard[0] + direction[guard[2]][0], guard[1] + direction[guard[2]][1]
  return isOnBoard(rr, cc) and grid[rr][cc] != "#"

def isNextOffBoard():
  rr, cc = guard[0] + direction[guard[2]][0], guard[1] + direction[guard[2]][1]
  return rr >= 0 and rr < len(grid) and cc >= 0 and cc < len(grid[0])

def isOnBoard(r, c):
  return r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0])

direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
visited = set()
count = 0

loop_spots = set()

while True:
  visited.add((guard[0], guard[1]))

  if canMove():
    rr, cc = guard[0] + direction[guard[2]][0], guard[1] + direction[guard[2]][1]

    copy = guard.copy()

    grid[rr][cc] = "#"
    if isLoop():
      loop_spots.add(tuple(guard))
    grid[rr][cc] = "."

    guard = copy.copy()

    guard[0], guard[1] = rr, cc
  elif not isOnBoard(guard[0] + direction[guard[2]][0], guard[1] + direction[guard[2]][1]):
    break
  else:
    guard[2] = (guard[2] + 1) % 4

  
print(len(visited))
print(len(loop_spots))

