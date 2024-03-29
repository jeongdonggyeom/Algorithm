from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
q = deque()

for _ in range(n):
    order = list(map(str, input().split()))

    if order[0] == "push":
        q.append(order[1])
    
    elif order[0] == "pop":
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    
    elif order[0] == "size":
        print(len(q))

    elif order[0] == "empty":
        if len(q) == 0:
            print(1)
        else:
            print(0)
    
    elif order[0] == "front":
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])

    elif order[0] == "back":
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])