def solution(stones, k):
    # deque를 써야 시간초과를 피할 수 있다.
    from collections import deque
    max_arr = deque([[stones[0], 0]])
    ans = [stones[0]]

    for i in range(1, len(stones)):
        while max_arr and max_arr[-1][0] < stones[i]:
            max_arr.pop()
        max_arr.append([stones[i], i])
        while i - max_arr[0][1] >= k:
            max_arr.popleft()
        ans.append(max_arr[0][0])
    return min(ans[k-1:])
#               0  1  2  3  4  5  6  7  8  9
print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3), 3)
print(solution([2, 4, 6, 5, 2, 1, 1], 3), 2)
print(solution([10, 7, 6, 8, 11], 3), 8)
print(solution([1, 2, 3, 4], 3), 3)
print(solution([4, 3, 2, 1], 3), 3)
print(solution([3, 3, 3, 3], 3), 3)
print(solution([1, 2, 3, 4], 1), 1)
print(solution([7, 2, 8, 7, 2, 5, 9], 3), 7)
print(solution([1, 2, 1, 1, 1, 2, 1], 3), 1)
print(solution([1, 2, 1, 2, 1, 2, 1], 2), 2)
print(solution([1], 1), 1)
print(solution([2], 1), 2)
print(solution([5,10], 2), 10)












