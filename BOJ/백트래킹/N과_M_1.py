n, m = map(int, input().split())
s = []

def aaa():
    if len(s) == m:
        for i in s:
            print(i, end=" ")
        print()
        return

    for i in range(1, n+1):
        if i not in s:
            s.append(i)
            aaa()
            s.pop()

aaa()