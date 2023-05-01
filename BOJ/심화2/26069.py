import sys
input = sys.stdin.readline

n = int(input().rstrip())
s = set()

for i in range(n):
    a, b = map(str, input().rstrip().split())
    if a == 'ChongChong' or b == 'ChongChong':
        s.add(a)
        s.add(b)
    elif a in s:
        s.add(b)
    elif b in s:
        s.add(a)

print(len(s))