a = int(input())
b = int(input())
c = int(input())

if a == b and b == c and a == 60:
    print('Equilateral')
elif (a+b+c) == 180:
    if a == b or b == c or a == c:
        print('Isosceles')
    if a != b and b != c and a != c:
        print('Scalene')
elif (a+b+c) != 180:
    print('Error')