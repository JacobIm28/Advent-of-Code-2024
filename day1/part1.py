leftIds = []
rightIds = []

with open('data.txt', 'r') as f:
  for line in f:
    ids = line.split(' ')
    leftIds.append(int(ids[0]))
    rightIds.append(int(ids[-1]))

leftIds.sort()
rightIds.sort()

totalDistance = 0

for l, r in zip(leftIds, rightIds):
  totalDistance += abs(l - r)

print(totalDistance)

