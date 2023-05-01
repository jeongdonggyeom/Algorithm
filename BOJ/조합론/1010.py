import math

n = int(input())

def asdf(a, b):
  c = math.factorial(a)
  d = math.factorial(a-b)
  e = math.factorial(b)

  print(c//(d*e))

for i in range(n):
    a, b = map(int, input().split())
    if a > b:
       asdf(a, b)
    else:
      asdf(b, a)
