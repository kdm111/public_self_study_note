class Solution:
    def minStoneSum(self, piles: list[int], k: int) -> int:
        # sol1 1783ms 80% 28.9MB 28%
        import heapq
        heap = [-stone for stone in piles]
        heapq.heapify(heap)
        for _ in range(k):
            curr = -heapq.heappop(heap)
            curr -= curr // 2
            heapq.heappush(heap, -curr)
        return -sum(heap)