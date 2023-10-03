'''
leet : 303 

클래스 NumArray는 sumRange라는 메소드를 제공한다.
sumRange는 left, right을 받아 그 사이의 합을 리턴한다.

# sol1
# 918ms 32% 19.6MB 97%
단순 합 리턴
# 당연히 이렇게 하는 걸 원하는 게 아니다.

# sol2
# 76ms 70% 19.9MB 61%
# 사전 합 
미리 O(n)을 소모하여 사전합을 구한뒤 right + 1에서 left를 제거한다.


'''
class NumArray:
    def __init__(self, nums: list[int]):
        # sol1
        self.numArr = nums[:]
        # sol2
        self.prefixSum = []
        temp = 0
        for num in nums:
            temp += num
            self.prefixSum.append(temp)


    def sumRange(self, left: int, right: int) -> int:
        # sol1
        # return sum(self.numArr[left: right+1])
        # sol2
        return self.prefixSum[right + 1] - self.prefixSum[left]

numArr = NumArray([-2, 0, 3, -5, 2, -1])
print(numArr.sumRange(0,3))