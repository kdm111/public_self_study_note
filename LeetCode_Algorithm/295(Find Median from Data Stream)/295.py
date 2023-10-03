import heapq
class MedianFinder:
    def __init__(self):
        self.heap = []

        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.heap, num)

    def findMedian(self) -> float:
        length = len(self.heap)
        if length % 2:
            return self.heap[length // 2]
        else:
            return (self.heap[length//2 - 1] + self.heap[length//2]) / 2

finder = MedianFinder()
finder.addNum(1)