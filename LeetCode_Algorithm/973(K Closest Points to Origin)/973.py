class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        # sol1 835ms 53% 20.5MB 36%
        import heapq
        heap = []
        for [x, y] in points:
            dist = x ** 2 + y ** 2
            heapq.heappush(heap, (-dist, [x,y]))
            if len(heap) > k:
                heapq.heappop(heap)
        return [[x,y] for (_, [x,y]) in heap]
    

print(Solution().kClosest([[1,3],[-2,2]], 1))