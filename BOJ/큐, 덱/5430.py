import sys
from collections import deque
input = sys.stdin.readline

t = int(input().rstrip())

for i in range(t):
    p = input().rstrip()
    n = int(input().rstrip())
    x = input().rstrip()
    q = deque(x[1:-1].split(","))
    r = 0
    flag = False
    if n == 0:
        q.clear()

    for j in p:
        if j == "R":
            r += 1
        elif j == "D":
            if len(q) == 0:
                print("error")
                flag = True
                break
            else:
                if r%2==0:
                    q.popleft()
                else:
                    q.pop()
                    
    if not flag:
        if r%2==1:
            q.reverse()
        print(f'[{",".join(q)}]')