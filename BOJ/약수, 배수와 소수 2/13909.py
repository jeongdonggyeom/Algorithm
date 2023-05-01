import sys
input = sys.stdin.readline

n = int(input().rstrip())

cnt = 0
i = 1
while i*i <= n:
    cnt += 1
    i += 1

print(cnt)