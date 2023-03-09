import sys

n = int(sys.stdin.readline().rstrip())
li = (list(map(int, input().split())))
del_li = sorted(list(set(li)))

compress = {del_li[i] : i for i in range(len(del_li))}

for i in li:
    print(compress[i], end=" ")