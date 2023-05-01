import sys
input = sys.stdin.readline

n = int(input())
n_d = {}
li = list(map(int, input().split()))

for i in li:
  try:
    n_d[i] += 1
  except KeyError:
    n_d[i] = 1

m = int(input())
li2 = list(map(int, input().split()))

for i in li2:
  try:
    print(n_d[i], end=" ")
  except KeyError:
    print(0, end=" ")