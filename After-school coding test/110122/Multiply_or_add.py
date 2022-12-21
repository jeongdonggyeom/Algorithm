import sys

li = int(sys.stdin.readline().rstrip())
li2 = []

while(li > 0):
    li2.append(li%10)
    li /= 10

print(li2)
