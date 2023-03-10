def solution(bridge_length, weight, truck_weights):
    answer = 0
    run = [0] * bridge_length

    while len(run):
        answer += 1
        run.pop(0)

        if truck_weights:
            if sum(run) + truck_weights[0] <= weight:
                run.append(truck_weights.pop(0))

            else:
                run.append(0)

    return answer

print(solution(2, 10, [7,4,5,6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))