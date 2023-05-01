n = int(input())

x = []
y = []

for i in range(n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

if len(x) == 1:
    print(0)
else:
    xpos = max(x) - min(x)
    ypos = max(y) - min(y)
    print(xpos * ypos)