n, m = map(int, input().split())
s = []

def aaa():
    if len(s) == m:
        for i in s:
            print(i, end=" ")
        print()
        return

    for i in range(1, n+1):
      if len(s) > 0:
          if s[-1] <= i:
              s.append(i)
              aaa()
              s.pop()
      else:
          s.append(i)
          aaa()
          s.pop()

aaa()