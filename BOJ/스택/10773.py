import sys
input = sys.stdin.readline

n = int(input().rstrip())

li = []

for i in range(n):
    a = int(input().rstrip())
    if a == 0:
        li.pop()
    else:
        li.append(a)

print(sum(li))