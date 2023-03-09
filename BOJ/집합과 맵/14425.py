import sys
input = sys.stdin.readline

a, b = map(int, input().split())
key = []
li = []
cnt = 0

for _ in range(a):
    key.append(input())

for _ in range(b):
    li.append(input())

for i in li:
    for j in key:
        if j in i:
            cnt += 1

print(cnt)