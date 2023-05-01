while True:
    a, b, c = map(int, input().split())
    li = [a, b, c]
    if a == 0:
        break
    
    ma = max(li)
    mi = min(li)
    li.pop(li.index(ma))
    li.pop(li.index(mi))

    if ma >= mi + li[0]:
       print('Invalid')

    elif a == b and b == c:
      print('Equilateral')
    elif a == b or b == c or a == c:
      print('Isosceles')  
    elif a != b and b != c and a != c:
      print('Scalene')