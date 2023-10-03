'''
LeetCode 2208 : Minimum Operations to Halve Array Sum

# sol1 1057ms 97% 28.9MB 34%
힙에서 최소 값을 제거한 뒤 그 값을 1/2로 나눠 totalSum에 더한다.

'''
class Solution:
    def halveArray(self, nums: list[int]) -> int:
        import heapq
        heap = [-num for num in nums]
        heapq.heapify(heap); totalSum = sum(nums) / 2 
        ans = 0
        while totalSum > 0:
            num = heapq.heappop(heap)
            heapq.heappush(heap, num / 2)
            totalSum += num / 2 
            ans += 1
        return ans
    
print(Solution().halveArray([5,19,8,1]))