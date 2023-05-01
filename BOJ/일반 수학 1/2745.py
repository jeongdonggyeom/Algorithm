n, b = map(str, input().split())
b = int(b)
sum = 0

for i in range(len(n)):
    temp = n[len(n) - (i + 1)]
    if temp >= '0' and temp <= '9':
      temp = ord(temp) - ord('0')
    else:
       temp = ord(temp) + 10 - ord('A')
    sum += (temp * int(b**i))

print(sum)