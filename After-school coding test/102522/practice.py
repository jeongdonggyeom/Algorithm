# 1 
# import sys

# n, m = map(int, sys.stdin.readline().split())
# l = [i for i in range(m, n+1) if i%m==0]
# print(sum(l))


# 2
# import sys

# n, m = map(int, sys.stdin.readline().split())
# sum=n
# print(n, end="")
# for i in range(n+1, m+1):
#     print(f" + {i}", end="")
#     sum+=i

# print(f" = {sum}")


# 3
# import sys

# n = int(sys.stdin.readline().rstrip())
# print(1, end="")
# l = [i for i in range(2, n) if n%i==0]
# for i in l:
#     print(f" + {i}", end="")
# print(f" = {sum(l)+1}")


# 4
# import sys

# a = sys.stdin.readline().rstrip()
# l = list(map(int, sys.stdin.readline().split()))
# print(max(l)-min(l))


# 5
# import sys

# a = sys.stdin.readline().rstrip()
# f, b = a.split("-")
# birth = int(f[0:2])
# bf = b[0]
# if(bf == "1"):
#     print(2020 - (1900 + birth), "M")
# elif(bf == "2"):
#     print(2020 - (1900 + birth), "W")
# elif(bf == "3"):
#     print(2020 - (2000 + birth), "M")
# elif(bf == "4"):
#     print(2020 - (2000 + birth), "W")


# 6
# import sys, re
# a = sys.stdin.readline().rstrip()
# numbers = int(re.sub(r'[^0-9]', '', a))
# l = [i for i in range(1, numbers+1) if numbers%i==0]
# print(numbers)
# print(len(l))



# 7
# import sys
# l = list(map(str, sys.stdin.readline().split()))
# str = ""
# for i in range(len(l)):
#     str += l[i]
# print(str.lower())


# 8
# import sys
# a = sys.stdin.readline().rstrip()
# left = right = 0
# if(a[0] == ")" or a[len(a)-1] == "("):
#     print("NO")
# else:
#     for i in range(len(a)):
#         if(a[i] == "("):
#             left+=1
#         elif(a[i] == ")"):
#             right+=1
#     if(left == right):
#         print("YES")
#     else:
#         print("NO")


# 9
# import sys
# a = int(sys.stdin.readline().rstrip())

# def func(n):
#     list = []
#     for i in range(1, int(n**(1/2)) + 1):
#         if (n % i == 0):
#             list.append(i) 
#             if ( (i**2) != n) : 
#                 list.append(n // i)
#     return list 

# for i in range(1, a+1):
#     if(i==1):
#         print(1, end=" ")
#     else:
#         print(len(func(i)), end=" ")


# 10
# import sys
# a = int(sys.stdin.readline().rstrip())
# l = list(map(str, sys.stdin.readline().split()))
# l2 = []

# for i in l:
#     sum = 0
#     for j in i:
#         sum = sum + int(j)
#     l2.append(sum)
#     sum=0

# if(l2.count(max(l2)) >= 2):
#     maxi=0
#     for i in range(0, l2.count(max(l2))):
#         if(maxi < int(l[l2.index(max(l2))])):
#             maxi = int(l[l2.index(max(l2))])
#         l2[l2.index(max(l2))] = 0
#     print(maxi)
# else: 
#     print(l[l2.index(max(l2))])


# 11
# import sys
# a = int(sys.stdin.readline().rstrip())
# result = 0
# for i in range(1, a+1):
#     if(i<10): 
#         result+=1
#     elif(i<100): 
#         result+=2
#     elif(i<1000): 
#         result+=3    
#     elif(i<10000): 
#         result+=4
#     elif(i<100000): 
#         result+=5
# print(result)


# 12
# import sys
# a = int(sys.stdin.readline().rstrip())
# result = 0
# for i in range(1, a+1):
#     if(i<10): 
#         result+=1
#     elif(i<100): 
#         result+=2
#     elif(i<1000): 
#         result+=3    
#     elif(i<10000): 
#         result+=4
#     elif(i<100000): 
#         result+=5
#     elif(i<1000000): 
#         result+=6
#     elif(i<10000000): 
#         result+=7
#     elif(i<100000000): 
#         result+=8
#     elif(i==100000000): 
#         result+=9

# print(result)


# 13
import sys
a = sys.stdin.readline().rstrip()
l = [0 for i in range(len(a))]

for i in a:
    l[int(i)]+=1

print(max(l))