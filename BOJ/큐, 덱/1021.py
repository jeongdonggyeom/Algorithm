import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
li = list(map(int, input().rstrip().split()))
q = deque([i for i in range(1, n+1)])
cnt = 0

while li:
    if li[0] == q[0]:
        del li[0]
        q.popleft()
    else:
        while li[0] != q[0]:
            f = 0
            r = 0
            for i in q:
                f += 1
                if i == li[0]:
                    break
            
            for i in reversed(q):
                r += 1
                if i == li[0]:
                    break
            
            if f > r:
                q.rotate(r)
                cnt += r
            else:
                cnt += f-1
                q.rotate(-f+1)
print(cnt)