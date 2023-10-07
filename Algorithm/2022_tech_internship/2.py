def solution(queue1, queue2):
    answer = 0
    queue1Sum = sum(queue1); queue2Sum = sum(queue2)
    totalSum = queue1Sum + queue2Sum
    if totalSum % 2 != 0:
        return -1
    goal = totalSum // 2
    i = j = k = 0;
    while j < len(queue2):
        if queue1Sum == goal:
            return answer 
        elif queue1Sum > goal:
            if i < len(queue1):
                queue1Sum -= queue1[i]
                i += 1; answer += 1
            elif j < len(queue2):
                queue1Sum -= queue2[j]
                j += 1; answer += 1
        elif queue1Sum < goal:
            queue1Sum += queue2[k]
            k += 1; answer += 1
    return -1

print(solution([3,2,7,2], [4,6,5,1]))
print(solution([1,2,1,2], [1,10,1,2]))
print(solution([1,1], [1,5]))

