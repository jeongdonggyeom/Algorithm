import sys
import math
input = sys.stdin.readline

a, b = map(int, input().split())
c, d = map(int, input().split())

denominator = b*d # 분모
numerator = c*b + a*d # 분자

while True:
  gcd = math.gcd(denominator, numerator)
  if gcd == 1:
    print(f'{numerator} {denominator}')
    break
  else:
    denominator //= gcd
    numerator //= gcd