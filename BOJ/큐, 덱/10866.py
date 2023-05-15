import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())
q = deque()

for i in range(n):
    a = input().rstrip().split(" ")

    if a[0] == 'push_back':
        q.append(a[1])
    elif a[0] == 'push_front':
        q.appendleft(a[1])
    elif a[0] == 'pop_front':
        print(q.popleft()) if len(q) > 0 else print(-1)
    elif a[0] == 'pop_back':
        print(q.pop()) if len(q) > 0 else print(-1)
    elif a[0] == 'size':
        print(len(q))
    elif a[0] == 'empty':
        print(1) if len(q) == 0 else print(0)
    elif a[0] == 'front':
        print(q[0]) if len(q) > 0 else print(-1)
    elif a[0] == 'back':
        print(q[-1]) if len(q) > 0 else print(-1)