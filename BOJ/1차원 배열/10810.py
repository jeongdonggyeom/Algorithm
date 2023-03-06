n, m = map(int, input().split())
li = [0 for _ in range(n)]

for _ in range(m):
    i,j,k = map(int, input().split())
    for l in range(i, j+1):
        li[l-1] = k
    
for i in range(n):
    print(li[i], end=" ")