import sys

n = int(sys.stdin.readline().rstrip())

for i in range(1, n+1):
    if n == i:
        print(0)
        break
    su = i + sum(list(map(int, str(i))))
    if su == n:
        print(i)
        break