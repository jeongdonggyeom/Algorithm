n, m = map(int, input().split())
li = [i for i in range(n+1)]
rot = [0 for i in range(n+1)]

for _ in range(m):
    begin, end, mid = map(int, input().split())
    for i in range(end-mid+1):
        rot[begin+i] = li[mid+i]
        
    for i in range(mid-begin):
        rot[begin+end-mid+1+i] = li[begin+i]

    for i in range(begin, end+1):
        li[i] = rot[i]
    

for i in range(n):
    print(li[i+1], end=" ")