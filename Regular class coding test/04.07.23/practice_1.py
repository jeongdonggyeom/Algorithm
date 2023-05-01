n = int(input())
li = list(map(int, input().split()))
sum = 0
result = 0

while li:
  sum += min(li)
  result += sum
  li.pop(li.index(min(li)))

print(result)
