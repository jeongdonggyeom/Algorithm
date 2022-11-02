#### 병합 정렬 (merge sort)
> ##### 병합 정렬이란 배열을 원소가 하나 남을때까지 반으로 쪼갠 후 크기 순으로 재배열하면서 원래 배열 크기로 합치는 정렬 알고리즘이다.
> ##### 병합 정렬은 분할정복법과 재귀 알고리즘을 사용한다.
> ##### 병합 정렬의 장점은 데이터 분포에 영향을 덜 받아 입력 데이터가 무엇이든 간에 정렬시간은 동일하다.
> ##### 병합 정렬의 단점은 만약 배열로 리스트를 구현할 경우 저장할 임시 배열이 필요하다. 
> ##### 제자리 정렬이 아니다. (in-place sorting)
> ##### 크기가 매우 큰 경우 이동 횟수가 많으므로 매우 큰 시간 낭비를 초래한다.
> ##### 예시로 1부터 8까지의 값이 담긴 배열을 병합정렬 해보겠다.
```python
1. [1, 3, 4, 5, 2, 7, 6, 8]
2. [1, 3, 4, 5] [2, 7, 6, 8]
3. [1, 3] [4, 5] [2, 7] [6, 8]
4. [1] [3] [4] [5] [2] [7] [6] [8]
```
> ##### 더이상 쪼갤 수 없으니 다시 합치기를 시작한다. 합칠때는 작은 숫자가 큰 숫자 앞으로 오게 한다.
```python
1. [1, 3] [4, 5] [2, 7] [6, 8]
2. [1, 3, 4, 5] [2, 6, 7, 8]
3. [1, 2, 3, 4, 5, 6, 7, 8]
```
> ##### 이렇게 정렬된 배열을 얻을 수 있다.
> ##### 그림으로 보면 이렇다.
<img src="https://www.programiz.com/sites/tutorial2program/files/merge-sort-example_0.png" width="300px" height="300px"></img>

> ##### 아래는 위에 설명한 방식을 python으로 구현한 코드이다.
```python
def merge_sort(arr):
    def sort(low, high):
        if high - low < 2:  # 만약 배열의 크기가 2 이하라면 작동 x
            return
        mid = (low + high)  # 반으로 나누기 위한 중간값
        sort(low, mid) # 원소가 하나가 남을 때 까지 쪼개기 위해 재귀호출
        sort(mid, high)
        merge(low, mid, high) # 쪼갠 배열을 정렬

    def merge(low, mid, high):
        temp = []
        l, h = low, mid

        while l < mid and h < high: # l가 mid를 넘어가거나 h가 배열의 크기를 벗어난다면 종료 
                                    # l이 mid를 넘어간다는 것은 왼쪽편에 있던 값이 모두 정렬된 것이기 때문 h도 마찬가지
            if arr[l] < arr[h]: # 크기 비교
                temp.append(arr[l])
                l += 1   # 인덱스 증가
            else:
                temp.append(arr[h])
                h += 1

        while l < mid: # 위에서 정렬하고 남은 값들을 모두 리스트에 넣기
            temp.append(arr[l])
            l += 1
        while h < high:
            temp.append(arr[h])
            h += 1

        for i in range(low, high): # 정렬한 배열을 기존 배열에 넣기
            arr[i] = temp[i - low]

    return sort(0, len(arr))
```

> ##### 병합 정렬의 시간복잡도는 O(NlogN)이다.
#### 참고
