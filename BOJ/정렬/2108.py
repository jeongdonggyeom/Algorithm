# f string을 이용해 소수점 반올림을 하니 틀렸다 하고 round 함수를 사용하니 정답이 나옴 왜???

import sys
from collections import Counter

n = int(sys.stdin.readline())
li = []

for _ in range(n):
    li.append(int(sys.stdin.readline()))

li.sort()
cnt = Counter(li)
order = cnt.most_common(2)

print(round(sum(li)/n))
print(li[n//2])
if len(order) > 1:
    if order[0][1] == order[1][1]:
        print(order[1][0])
    else: 
        print(order[0][0])
else:
    print(order[0][0])
print(max(li)-min(li))