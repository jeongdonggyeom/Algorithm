import sys
input = sys.stdin.readline

a, b = map(int, input().split())
key = set()
cnt = 0

for i in range(a):
    key.add(input())

for i in range(b):
    k = input()
    if k in key:
        cnt += 1

print(cnt)