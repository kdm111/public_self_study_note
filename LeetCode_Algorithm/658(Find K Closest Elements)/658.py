'''
LeetCode 658 : Find K Closest Elements
정렬된 배열이 존재할 때 k,x라는 두 개의 정수가 주어진다.
x에 가장 가까운 k개의 정수를 리턴하라
반드시 오름차순이여야 한다.

# sol1

'''
class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        # sol1 407ms 18% 16.6MB 7%
        import heapq
        heap = []
        for num in arr:
            val = abs(x - num)
            heapq.heappush(heap, (-val, -num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return sorted(-val for [_, val] in heap)

print(Solution().findClosestElements([1,2,3,4,5], 4, 3))
print(Solution().findClosestElements([1,2,3,4,5], 4, -1))

