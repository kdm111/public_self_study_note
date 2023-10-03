'''
LeetCode 2229 : Check if an Array Is Consecutive
주어진 배열의 숫자가 배열의 길이만큼 연속적인지 확인하라
예 [3,5,4] true

# sol1 1080ms 62% 29.1MB 57%
O(n) O(1)
set으로 치환해서 찾는 속도를 줄이고 하나씩 더해가며 set에 주어진 수가 존재하는 지 찾는다.

# sol2 551~1180ms 100~18% 29.2MB 44%
O(n) O(1)
주어진 숫자의 구간을 구한 뒤 배열의 길이와 셋의 길이를 구함
'''
from typing import List
class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        # sol1
        # length = len(nums); num = min(nums)
        # nums = set(nums)
        # i = 0; 
        # while i < length:
        #     if num+i not in nums:
        #         return False
        #     i += 1
        # return True

        # sol2
        return max(nums) - min(nums) + 1 == len(nums) == len(set(nums))
