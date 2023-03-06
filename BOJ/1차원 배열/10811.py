n, m = map(int, input().split())
li = [i for i in range(n+1)]

for l in range(m):
    i,j = map(int, input().split())
    while i<j:
        li[i], li[j] = li[j], li[i]
        i+=1
        j-=1

for i in range(n):
    print(li[i+1], end=" ")