import enum
from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # sol1 O(n), O(1) 158~203ms 73 46%
        # n의 길이 라면 n(n+1)/2 
        # 배열을 돌면서 뺀 값을 리턴
        # n = len(nums)
        # sum_len_nums = int(n*(n+1)/2)
        # return sum_len_nums-sum(num for num in nums)

        # sol2 O(nlogn) O(1) 171~213ms 66~43%
        # sort
        # nums.sort()
        # for i in range(len(nums)):
        #     if i != nums[i]: return i
        # return len(nums)

        # sol3 O(n), O(n)
        # hashSet
        # hashSet = set(nums)
        # n = len(nums)+1
        # for number in range(n):
        #     if number not in hashSet: return number

        # sol4 O(n), O(1) 206 47
        # bit manipulation
        # 인덱스와 숫자간의 비트 조작을 통해 문제를 해결할 수도 있다.
        
        # n ^ n = 0
        # 0 ^ n = n
        # idx : 0 1 2 3
        # num : 0 1 3 4
        # total length : 4
        # (0^0) ^ (1^1) ^ (3^3) ^ (4^4) ^ 2 = 0 ^ 0 ^ 0 ^ 0 ^ 2
        
        # 전체 인덱스 + 전체 숫자 + 총 길이를 모두 xor 연산한다.
        ans = len(nums)
        for idx, num in enumerate(nums):
            ans ^= idx ^ num
        return ans







print(Solution().missingNumber([3,0,1]))