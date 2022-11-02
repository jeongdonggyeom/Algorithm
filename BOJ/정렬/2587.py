import sys

li = []

for _ in range(0, 5):
    a = int(sys.stdin.readline().rstrip())
    li.append(a)

li.sort()

print(sum(li)//len(li))
print(li[(len(li)//2)])