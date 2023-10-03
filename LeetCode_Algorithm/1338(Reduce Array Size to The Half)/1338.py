'''
LeetCode 1338 : Reduce Array Size to The Half
정수 배열이 주어지고 숫자를 선택하여 배열에 나타난 모든 숫자를 지울 수 있다.
적어도 최소한 길이가 1/2이 되게 지우는 숫자의 수를 구하라

# sol1 599ms 65% 32.3MB 62.68%
카운터를 사용해서 가장 많이 나타난 숫자를 제거한다.

'''
class Solution:
    def minSetSize(self, arr: list[int]) -> int:
        from collections import Counter
        import heapq
        counter = Counter(arr); 
        total_length = len(arr); goal = total_length / 2
        heap = []
        for (_, v) in counter.items():
            heap.append(-v)
        heapq.heapify(heap)
        ans = 0
        while goal < total_length:
            total_length += heapq.heappop(heap)
            ans += 1
        return ans


print(Solution().minSetSize([3,3,3,3,5,5,5,2,2,7]))