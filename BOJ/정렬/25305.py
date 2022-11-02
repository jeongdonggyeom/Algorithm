import sys

N, k = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))

li.sort(reverse=True)
print(li[k-1])