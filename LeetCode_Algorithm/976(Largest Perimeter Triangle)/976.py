'''
LeetCode 976 : Largest Perimeter Triangle
숫자 리스트가 들어올 때 해당 숫자 3개로 구성할 수 있는 가장 큰 삼각형의 둘레 구하기

sol1 184ms 99% 15.4MB 45.8%
O(nlogn) O(1)
세 변이 a,b,c(a <= b <= c)라고 할 때 
삼각형의 공식은 a+b > c를 조건으로 갖추어야 한다.
'''
from typing import List
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums)-2):
            if nums[i] < nums[i+1] + nums[i+2]:
                return nums[i] + nums[i+1] + nums[i+2]
        return 0