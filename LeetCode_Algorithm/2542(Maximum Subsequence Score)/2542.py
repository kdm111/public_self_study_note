class Solution:
    def maxScore(self, nums1: list[int], nums2: list[int], k: int) -> int:
        import heapq
        # sol1 845ms 95% 37.7MB 57%
        total = ans = 0; heap = []
        for a, b in sorted(list(zip(nums1, nums2)), key=lambda x : -x[1]):
            total += a
            heapq.heappush(heap, a)
            if len(heap) > k:
                total -= heapq.heappop(heap)
            if len(heap) == k:
                ans = max(ans, total * b)
        return ans
        

print(Solution().maxScore([1,3,3,2], [2,1,3,4], 3))
        
        