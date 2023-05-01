import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dict1 = {input().rstrip() : i for i in range(1, n+1)}
dict1_reverse = dict(map(reversed, dict1.items()))

for i in range(m):
    q = input().rstrip()
    if q in dict1.keys():
        print(dict1[q])
    else:
        print(dict1_reverse[int(q)])