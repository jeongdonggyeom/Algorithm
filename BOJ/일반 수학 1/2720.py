import sys
input = sys.stdin.readline

n = int(input())
li = [25, 10, 5, 1]

for i in range(n):
    a = int(input())
    for j in li:
        print(a//j, end=" ")
        a %= j
    print()