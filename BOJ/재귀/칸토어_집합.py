def sss(a):
    if a == 1:
        return '-'
    b = a // 3
    return sss(b)+" "*b+sss(b)

while True:
    try:
        n = int(input())
        a = 3**n
        print(sss(a))
    except:
        break