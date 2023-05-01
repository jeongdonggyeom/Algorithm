li = list(map(str, input().split()))
str_li = []
num_li = []


def sort_str(li):
  copy_li = li[:]
  new_str_li = []
  for idx, str in enumerate(li):
    new_str_li.append((idx, str.lower()))
  new_str_li.sort()
  print(new_str_li)

  for i in new_str_li:
     li[i[0]] = copy_li[i[0]]

def sort_num(li):
  

for i in li:
    new_str = ''
    new_num = ''
    for j in i:
        if ord(j) >= 65 and ord(j) <= 90 or ord(j) >= 97 and ord(j) <= 122 and new_num == '':
          new_str += j
        elif ord(j) >= 48 and ord(j) <= 57:
          new_num += j
        elif new_num != '' and not (ord(j) >= 48 and ord(j) <= 57):
           break
    str_li.append(new_str)
    num_li.append(new_num)

sort_str(str_li)
print(str_li)


"""
"img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"

1. 문자열, 숫자 나누기
  - 문자열은 숫자가 나오기 전까지 입력
  - 숫자는 뒤에 숫자가 아닌 문자가 나오기 전까지 입력

2. 문자열 정렬
  - 입력 리스트 복사하고 이름을 copy_li라고 함
  - 소문자 문자열, 인덱스로 이루어진 튜플이 담긴 리스트를 new_str_li라는 이름으로 만듬
  - sort()로 정렬
  - new_str_li의 인덱스에 따라 str_li에 copy_li의 문자열을 삽입

3. 숫자 정렬
  - rngus TLqkf
"""

