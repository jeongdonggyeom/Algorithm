import sys
import math
input = sys.stdin.readline

n = int(input().rstrip())

def isPrime(a):
    for i in range(2, int(math.sqrt(a))+1):
        if a % i == 0:
            return False
    return True


for _ in range(n):
    a = int(input().rstrip())
    if a == 1 or a == 0:
        print(2)
        continue
    while True:
        if isPrime(a):
            print(a)
            break
        else:
            a += 1