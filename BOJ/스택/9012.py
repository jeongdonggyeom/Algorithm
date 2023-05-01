import sys
input = sys.stdin.readline

n = int(input().rstrip())


for i in range(n):
    li = []
    flag = True
    a = input().rstrip()
    for i in a:
        if i == '(':
            li.append(i)
        elif i == ')':
            if len(li) == 0:
                print("NO")
                flag = False
                break
            else:
                li.pop()
    if flag:
      if len(li) == 0: 
        print("YES")
      else:
        print("NO")