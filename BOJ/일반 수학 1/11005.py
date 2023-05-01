n, b = map(int, input().split())
sum = ''

while n:
  if n%b >= 10:
    sum += chr(n%b+55)
  else:
    sum += str(n%b)
  n //= b

print(sum[::-1])