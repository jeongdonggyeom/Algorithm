n, m = map(int, input().split())
li = list(map(int, input().split()))

s = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            plus = li[i] + li[j] + li[k]
            if plus > s and plus <= m:
                s = plus

print(s)
