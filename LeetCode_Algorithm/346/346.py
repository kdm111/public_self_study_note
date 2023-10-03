from collections import deque

class MovingAverage:
    # sol1
    # circular queue 
    # 86~103 74~56%
    def __init__(self, size: int):
        self.nums = [None] * size
        self.front = 0
        self.rear = -1
        self.size = size

        self.length = 0
        self.totalSum = 0

    def next(self, val: int) -> float:

        self.rear = (self.rear+1) % self.size
        
        if self.nums[self.rear]:
            self.totalSum -= self.nums[self.front]
            self.nums[self.front] = None
            self.length -= 1
            self.front = (self.front+1) % self.size
            
    
        self.nums[self.rear] = val
        self.length += 1
        self.totalSum += val
        
        return self.totalSum / self.length
        

mv = MovingAverage(3)
print(mv.next(1))
print(mv.nums)

print(mv.next(2))
print(mv.nums)

print(mv.next(3))
print(mv.nums)

print(mv.next(4))
print(mv.nums)

print(mv.next(5))
print(mv.nums)

print(mv.next(6))
print(mv.nums)

print(mv.next(7))
print(mv.nums)



