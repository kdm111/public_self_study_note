from operator import truediv
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # sol1 brute-force n^2 시간초과

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]: return True
        # return False

        # sol2 nlogn 500~900ms 50% 10%        
        # nlogn으로 sorting한 이후 n으로 읽어가면서 같은 숫자가 보이면 true를 리턴

        # nums.sort()
        # for i in range(len(nums)-1):
        #     if nums[i] == nums[i+1]: return True
        # return False

        # sol3 n 400~500ms 90%~80% 보다 빠름
        # O(n) 해쉬맵을 이용하여 카운트, 해쉬맵에서 존재했다면 true를 리턴
        # checkMap = {}
        # for i in nums:
        #     if checkMap[i]:
        #         checkMap[i] = 1
        #     else:
        #         return True
        # return False
        
        # sol4 n
        # set을 활용하여 set의 길이 == nums의 길이 확인
        return False if len(set(nums))==len(nums) else True



print(Solution().containsDuplicate([1,2,3,4]))