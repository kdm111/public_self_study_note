import heapq
from typing import List
class Heap():
    def __init__(self, items):
        self.items = items
        # 중간에서 부터 뒤에 있는 자식 노드를 확인한다.
        for idx in range(len(self.items)//2, -1, -1):
            self.makeheap(self.items, idx)

    def makeheap(self, items, idx):
        largest = idx
        left = 2*largest+1
        right = 2*largest+2
        # 가장 큰 값이 오도록 바꿈
        if left < len(self.items) and items[left] > items[largest]:
            largest = left
        if right < len(self.items) and items[right] > items[largest]:
            largest = right
        if largest != idx:
            items[largest], items[idx] = items[idx], items[largest]
            self.makeheap(items, largest)

    def heap_add(self, num):
        self.items.append(num)
        for idx in range(len(self.items)//2, -1, -1):
            self.makeheap(self.items, idx)
    def heap_pop(self):
        num = self.items.pop(0)
        for idx in range(len(self.items)//2, -1, -1):
            self.makeheap(self.items, idx)
        return num

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # # sol1 time limit exceeded 5000개
        # # O(n)으로 k번째로 큰 수 찾기
        # heap = Heap(nums)
        # # max heap을 구현해서 그만큼 pop
        # for _ in range(k):
        #     num = heap.heap_pop()
        # return num
        
        # sol2 random select
        # O(n) 875ms 25%
        # if not nums: return ;
        # import random
        # pivot = random.choice(nums)
        # left = [x for x in nums if x > pivot]
        # mid = [x for x in nums if x == pivot]
        # right = [x for x in nums if x < pivot]
        # l = len(left); m = len(mid)
        # # k가 임의의 개수보다 더 작으면
        # if k <= l:
        #     return self.findKthLargest(left, k)
        # # 현재 k가 더 크다면 그만큼 큰 수 만큼 제거 한뒤 
        # elif k > l+m:
        #     return self.findKthLargest(right, k-l-m)
        # else:
        #     return mid[0]

        # sol3 heapq
        # 459ms 86% 29.27MB 89%
        import heapq
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]

print(Solution().findKthLargest([3,2,1,5,6,4], 2))