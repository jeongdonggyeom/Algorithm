import sys

input = sys.stdin.readline

n = int(input().rstrip())
li = [0]
answer = []
m = 0
flag = True

for _ in range(n):
    a = int(input().rstrip())

    if li[-1] == a:
        li.pop()
        answer.append("-")
    elif li[-1] != a and a in li:
        print("NO")
        flag = False
        break
    else:
        for i in range(m + 1, a + 1):
            li.append(i)
            answer.append("+")
        m = li.pop()
        answer.append("-")

if flag:
    for i in answer:
        print(i)