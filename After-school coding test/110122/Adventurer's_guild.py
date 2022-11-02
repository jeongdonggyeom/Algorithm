import sys
a = int(sys.stdin.readline().rstrip())
li = list(map(int, sys.stdin.readline().split()))
cnt=0

li.sort(reverse=True)
for i in li:
    if((a-i)>=0):
        a-=i
        cnt+=1
print(cnt)