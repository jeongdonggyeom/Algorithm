import sys

input = sys.stdin.readline

while True:
    a = input().rstrip()
    li = []

    if a == ".":
        break

    for i in a:
        if i == "[" or i == "(":
            li.append(i)
        elif i == "]":
            if len(li) != 0 and li[-1] == "[":
                li.pop()
            else:
                li.append("]")
                break
        elif i == ")":
            if len(li) != 0 and li[-1] == "(":
                li.pop()
            else:
                li.append(")")
                break
    if len(li) == 0:
        print("yes")
    else:
        print("no")
