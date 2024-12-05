rules = {}

doneRules = False

correct = []
total = 0

incorrectTotal = 0

def topologicalSortUtil(v,visited,stack):
  # Mark the current node as visited.
  visited[v] = True

  # Recur for all the vertices adjacent to this vertex
  for i in rules[v]:
    if i in visited and visited[i] == False:
      topologicalSortUtil(i,visited,stack)

  # Push current vertex to stack which stores result
  stack.insert(0,v)

def topologicalSort(pages):
  # Mark all the vertices as not visited
  visited = {
  }

  for page in pages:
    visited[page] = False

  stack = []

  # Call the recursive helper function to store Topological
  # Sort starting from all vertices one by one
  for page in pages:
    if visited[page] == False:
      topologicalSortUtil(page,visited,stack)

  # Print contents of stack
  return stack

def getMiddleInTopoOrder(pages):
  # print(rules)
  topo = topologicalSort(pages)
  # print(topo)

  pageTopo = []

  for pg in topo:
    if pg in pages:
      pageTopo.append(pg)
  
  print(pageTopo)
  return int(pageTopo[len(pageTopo) // 2])

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
          incorrectTotal += getMiddleInTopoOrder(pages)
      else:
        fro, to = line.strip().split('|')
        if fro not in rules:
          rules[fro] = set()
        rules[fro].add(to)

print(incorrectTotal)

# ['13', '93', '86', '19', '98', '77', '15']
# ['98', '77', '15', '93', '13', '86', '19']