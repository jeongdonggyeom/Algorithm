credit = 0
grade = 0
multiple = 0

for _ in range(20):
    a,b,c = map(str, input().split())

    if c[0] == 'P':
        continue

    credit += float(b)
    if c[0] == 'A':
        multiple = 4.0
        if c[1] == '+':
            multiple += 0.5
    elif c[0] == 'B':
        multiple = 3.0
        if c[1] == '+':
            multiple += 0.5
    elif c[0] == 'C':
        multiple = 2.0
        if c[1] == '+':
            multiple += 0.5
    elif c[0] == 'D':
        multiple = 1.0
        if c[1] == '+':
            multiple += 0.5
    elif c[0] == 'F':
        multiple = 0

    grade += float(b)*multiple

print(f'{(grade/credit):.6f}')