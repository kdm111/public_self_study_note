class maxHeap:
    def __init__(self, val, hashMap):
        self.arr = []
        self.size = val
        self.hashMap = hashMap
    def getPar(self, val):
        return (val-1) // 2
    def getLeftChild(self, val):
        return 2 * val + 1
    def getRightChild(self, val):
        return 2 * val + 2
    def heappush(self, val):
        self.arr.append(val)
        self.heapifyup()
    def heapifyup(self):
        i = len(self.arr)-1
        while self.getPar(i) >= 0 and self.hashMap[self.arr[self.getPar(i)]] < self.hashMap[self.arr[i]]:
            self.arr[self.getPar(i)], self.arr[i] = self.arr[i], self.arr[self.getPar(i)]
            i -= 1
        
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # sol1
        # hashMap = {}
        # for num in nums:
        #     if num not in hashMap:
        #         hashMap[num] = 1
        #     else:
        #         hashMap[num] += 1
        # heap = maxHeap(k, hashMap)
        # for k in hashMap:
        #     heap.heappush(k)
        # return heap.arr[:k-1]

        # sol2 108ms 59% 18.6MB 88%
        from collections import defaultdict
        import heapq
        heap = []; hashMap = defaultdict(int)
        for num in nums:
            hashMap[num] += 1
        for key, val in hashMap.items():
            heapq.heappush(heap, (val, key))
            if len(heap) > k:
                heapq.heappop(heap)
        return [key for [ _, key] in heap]
            
        
            
        
        

print(Solution().topKFrequent([-1,1,4,-4,3,5,4,-2,3,-1], 3))
print(Solution().topKFrequent([4,1,-1,2,-1,2,3], 2))
