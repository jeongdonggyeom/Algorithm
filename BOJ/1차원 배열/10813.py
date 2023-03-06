n, m = map(int, input().split())
li = [i for i in range(n+1)]

for _ in range(m):
    i, j = map(int, input().split())
    li[i], li[j] = li[j], li[i]

for i in range(n):
    print(li[i+1], end=" ")