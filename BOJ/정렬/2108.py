import sys
from collections import Counter

n = int(sys.stdin.readline())
li = []

for _ in range(n):
    li.append(int(sys.stdin.readline()))

li.sort()
cnt = Counter(li)
order = cnt.most_common()

print(f'{sum(li)/n:.0f}')
print(li[n//2])
if len(order) >= 2:
    print(order[1][0])
else:
    print(order[0][0])
print(max(li)-min(li))