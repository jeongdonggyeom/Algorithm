import sys
input = sys.stdin.readline

a = int(input().rstrip())
prime = [1 for _ in range(1000001)]

for i in range(2, 1001):
    for j in range(i*2, 1000001, i):
        prime[j] = 0

for i in range(a):
    b = int(input().rstrip())
    one, two = 0, 0
    s = set()
    for j in range(2, b):
       if prime[j] and prime[b-j] and b-j != 1:
          if j > b-j:
            one = b-j
            two = j
          else:
            one = j
            two = b-j
          s.add((one, two))
    print(len(s))