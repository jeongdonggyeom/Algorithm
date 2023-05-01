import sys
import math
input = sys.stdin.readline

n = int(input())
cnt = 0
li = []
li2 = []

li.append(int(input().rstrip()))

for i in range(1, n):
    li.append(int(input().rstrip()))
    li2.append(li[i]-li[i-1])

g = li2[0]

for i in range(1, len(li2)):
    g = math.gcd(li2[i], g)

for i in li2:
    cnt += (i // g) - 1

print(cnt)