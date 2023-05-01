n = int(input())
li = list(map(int, input().split()))

for i in range(n):
  max_idx = i
  for j in range(i + 1, n):
    if li[j] > li[max_idx]:
      max_idx = j
  li[i], li[max_idx] = li[max_idx], li[i]
	
for i in li:
  print(i, end=" ")