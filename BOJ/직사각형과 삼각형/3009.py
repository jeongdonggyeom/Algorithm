x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

def asdf(a, b, c):
    if a == b:
      return c
    elif a == c:
       return b
    else:
       return a
    
print(asdf(x1, x2, x3), end=" ")
print(asdf(y1, y2, y3))