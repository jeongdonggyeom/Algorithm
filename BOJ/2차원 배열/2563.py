arr = [[0 for i in range(100)] for j in range(100)]
cnt = 0

n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    
    for i in range(10):
        for j in range(10):
            arr[y+i][x+j] = 1

for i in arr:
    cnt += i.count(1)

print(cnt)