import sys
input = sys.stdin.readline

a = input().rstrip()
s = set()

for i in range(len(a)):
    for j in range(i, len(a)):
        li = a[i:j+1]
        s.add(li)

print(len(s))