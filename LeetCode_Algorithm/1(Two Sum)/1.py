from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # sol1
        hash_table = {}
        for idx,num in enumerate(nums):
            match_num = target - num
            if match_num in hash_table:
                return [idx, hash_table[match_num]]     
            hash_table[num] = idx

        # sol2 n^2 시간 제한 
        # for i in range(len(nums)-1):
        #     for j in range(1, len(nums)):
        #         if i!= j and nums[i] + nums[j] == target:
        #             return [i,j]

print(Solution().twoSum([1,2,3], 4))
print(Solution().twoSum([2,7,11,15], 9))

