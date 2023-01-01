a, b = map(int, input().split())

arr = []

for i in range(a):
    arr.append(list(map(int, input().split())))

for i in range(a):
    li = list(map(int, input().split()))
    for j in range(b):
        arr[i][j] += li[j]

for i in range(a):
    for j in range(b):
        print(arr[i][j], end=" ")
    print()