import sys

li = list(map(int, sys.stdin.readline().split()))

for i in range(1, 31):
    if(li.count(i)==0):
        print(i)
