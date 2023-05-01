import sys
input = sys.stdin.readline

n, m = map(int, input().split())

s1 = set(list(map(int, input().split())))
s2 = set(list(map(int, input().split())))

r1 = s1 - s2
r2 = s2 - s1

print(len(r1 | r2))