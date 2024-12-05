rules = {}

doneRules = False

correct = []
total = 0

with open('data.txt') as f:
  for line in f:
    if len(line.strip()) == 0:
      doneRules = True
    else:
      if doneRules:
        pages = line.strip().split(',')

        isCorrect = True

        for i, page in enumerate(pages):
          if page not in rules:
            continue
          for after in rules[page]:
            if after in pages and pages.index(after) < i:
              isCorrect = False
              break
        
        if isCorrect:
          total += int(pages[len(pages) // 2])
      else:
        fro, to = line.strip().split('|')
        if fro not in rules:
          rules[fro] = set()
        rules[fro].add(to)

print(total)

# ['13', '93', '86', '19', '98', '77', '15']
# ['98', '77', '15', '93', '13', '86', '19']