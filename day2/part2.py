def isReportSafe(report):
  l = len(report)

  if l <= 1:
    return True
  elif l <= 2:
    return report[0] != report[1]
  elif report[0] == report[1]:
    return False
  
  decreasing = report[0] > report[1]
  increasing = report[0] < report[1]

  for i in range(1, l):
    if 1 > abs(report[i] - report[i-1]) or abs(report[i] - report[i-1]) > 3:
      return False

    if decreasing and report[i-1] < report[i]:
      return False
    
    if increasing and report[i-1] > report[i]:
      return False
  
  return True

safeCount = 0

print('counting safe reports...')

with open('data.txt', 'r') as f:
  for line in f:
    report = [int(x) for x in line.split(' ')]

    for i in range(len(report)):
      copy = report.copy()
      copy.pop(i)
      if isReportSafe(copy):
        safeCount += 1
        break

print(safeCount)


