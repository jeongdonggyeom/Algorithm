import sys

n = int(sys.stdin.readline())
li = []
rank = [0] * n

for _ in range(n):
    a, b = map(int, input().split())
    li.append((a, b))

for i in range(len(li)):
    cnt = 1
    for j in range(len(li)):
        if i==j:
            continue
        if li[i][0] < li[j][0] and li[i][1] < li[j][1]:
            cnt += 1
    rank[i] = cnt

for i in rank:
    print(i, end=" ")