import sys
from collections import deque

input = sys.stdin.readline

t = int(input().rstrip())

for i in range(t):
    n, m = map(int, input().rstrip().split())
    a = list(map(int, input().rstrip().split()))
    q = deque(a)
    
    