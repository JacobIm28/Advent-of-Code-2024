leftCounts = {}
rightCounts = {}

with open('data.txt', 'r') as f:
  for line in f:
    ids = line.split(' ')
    leftId, rightId = int(ids[0]), int(ids[-1]) 

    if leftId not in leftCounts:
      leftCounts[leftId] = 0
    if rightId not in rightCounts:
      rightCounts[rightId] = 0

    leftCounts[leftId] += 1
    rightCounts[rightId] += 1

similarityScore = 0

for leftId, count in leftCounts.items():
  similarityScore += leftId * count * rightCounts.get(leftId, 0)

# for rightId, count in rightCounts.items():
#   similarityScore += rightId * count * leftCounts.get(rightId, 1)

print(similarityScore)


