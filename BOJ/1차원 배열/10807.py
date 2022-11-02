import sys

a = sys.stdin.readline().rstrip()
li = list(map(int, sys.stdin.readline().split()))
key = int(sys.stdin.readline().rstrip())

print(li.count(key))