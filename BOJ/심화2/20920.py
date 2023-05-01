import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

d = {}

for i in range(n):
    a = input().rstrip()
    if len(a) < m:
        continue
    if a in d.keys():
        d[a] += 1
    else:
        d[a] = 1

d_s = sorted(d.items(), key=lambda x : (-x[1], -len(x[0]), x[0]))
for i in d_s:
    print(i[0])