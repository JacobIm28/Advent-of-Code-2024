

with open('data.txt', 'r') as f:
  s = "".join(f.read().strip().split('\n'))

i = 0
l = len(s)

def readMult(i):
  if s[i:i+4] != 'mul(':
    return i, 0

  j = i + 4
  while s[j] in "1234567890":
    j += 1
  
  if s[j] != ',':
    return j - 1, 0
  
  firstNum = int(s[i+4:j])

  k = j + 1

  while s[k] in "1234567890":
    k += 1
  
  if s[k] != ')':
    return k - 1, 0
  
  secondNum = int(s[j+1:k])

  return k, firstNum * secondNum

total = 0

while i < l:
  new_i, val = readMult(i)
  print(i, new_i, val)
  total += val
  i = new_i + 1

print(total)
