import sys
input = sys.stdin.readline

n, m = map(int, input().split())

s1 = set([input().rstrip() for _ in range(n)])
s2 = set([input().rstrip() for _ in range(m)])

result = s1 & s2
a = sorted(result)

print(len(result))
for i in a:
    print(i)