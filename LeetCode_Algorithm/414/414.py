from logging import root
from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # 112ms 9%
        # nums = sorted(set(nums), reverse=True)
        # return nums[2] if len(nums) >= 3 else nums[0]


        # custom heap 108ms 11%
    #     heap = []
    #     for num in nums:
    #         if num in heap:
    #             continue
    #         elif len(heap) < 3:
    #             heap.append(num)
    #         elif len(heap) >= 3 and heap[2] < num:
    #             heap[2] = num
    #         self.swap(heap)
    #     return heap[2] if len(heap) >= 3 else heap[0]

    # def swap(self, heap):
    #     root = 0
    #     left = 1
    #     right = 2
        
    #     if 3 <= len(heap) and heap[right] > heap[left]:
    #         heap[left], heap[right] = heap[right], heap[left]
    #     if 2 <= len(heap) and heap[left] > heap[root]:
    #         heap[root], heap[left] = heap[left], heap[root]



        # set 107ms 12%
        # maximums = set()
        # for num in nums:
        #     maximums.add(num)
        #     if len(maximums) > 3:
        #         maximums.remove(min(maximums))
        # return min(maximums) if len(maximums) == 3 else max(maximums)
        
        # heapifiy 68ms 58%
        import heapq
        nums = list(set(nums))
        heapq.heapify(nums)
        while len(nums) > 3:
            heapq.heappop(nums)
        return nums[0] if len(nums) == 3 else nums[-1]

        
        

        


print(Solution().thirdMax([1,2,3,4,5,6]))
            