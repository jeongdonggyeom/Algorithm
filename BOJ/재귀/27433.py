import sys
input = sys.stdin.readline

def aaa(n):
    if n <= 1:
        return 1
    return n * aaa(n-1)
    
n = int(input().rstrip())
print(aaa(n))