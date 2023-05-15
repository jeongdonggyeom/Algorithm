b = 0

def recursion(s, l, r):
    global b
    b += 1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: 
        return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

n = int(input())

for i in range(n):
    a = input()
    b = 0
    result = isPalindrome(a)
    print(f'{result} {b}')