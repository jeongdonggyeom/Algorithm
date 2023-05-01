bracket = list(input())

li = []
answer = 0
tmp = 1

for i in range(len(bracket)):
  if bracket[i] == "(":
    li.append(bracket[i])
    tmp *= 2

  elif bracket[i] == "[":
    li.append(bracket[i])
    tmp *= 3

  elif bracket[i] == ")":
    if not li or li[-1] == "[":
      answer = 0
      break
    if bracket[i-1] == "(":
      answer += tmp
      
    li.pop()
    tmp //= 2

  else:
    if not li or li[-1] == "(":
      answer = 0
      break
    if bracket[i-1] == "[":
      answer += tmp

    li.pop()
    tmp //= 3

if li:
  print(0)
else:
  print(answer)