import collections as col

def solution(participant, completion):
    dic = col.Counter(participant)

    for i in completion:
        if i in dic and dic.get(i) != 0:
            dic[i] = dic.get(i) - 1
    
    for i, j in dic.items():
        if j == 1:
            return i


# solution(["leo", "kiki", "eden"], ["eden", "kiki"])
# solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"])
# solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])