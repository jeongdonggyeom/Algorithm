import sys
from collections import deque

input = sys.stdin.readline

t = int(input().rstrip())

for i in range(t):
    n, m = map(int, input().rstrip().split())
    li = list(map(int, input().rstrip().split()))
    key = li[m]
    q = deque(li)
    cnt = 0
    while True:
        cnt += 1
        ma = max(q)
        while q[0] != ma:
            q.append(q.popleft())
            if m == 0:
                m = len(q) - 1
            else:
                m -= 1
        
        if q[0] == key and m == 0:
            break
        q.popleft()
        m -= 1
    print(cnt)