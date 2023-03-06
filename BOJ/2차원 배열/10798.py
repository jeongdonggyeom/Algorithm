li = [input().split() for _ in range(5)]
arr = [[-1 for i in range(15)] for j in range(15)]
result = ""
x = 0

for i in li:
    for j in range(len(i[0])):
        arr[j][x] = i[0][j]
    x += 1

for i in arr:
    for j in i:
        if j != -1:
            result += j

print(result)