a = input()

num = []
eng = []

for i in a:
	if ord(i) >= 48 and ord(i) <= 57:
		num.append(int(i))
	else:
		eng.append(i)
		
for i in sorted(eng):
	print(i, end="")

print(sum(num))