def solution(clothes):
    answer = 1
    li = [y for x, y in clothes]
    count = [li.count(y) for y in set(li)]
    for i in count:
        answer *= i + 1

    return answer - 1