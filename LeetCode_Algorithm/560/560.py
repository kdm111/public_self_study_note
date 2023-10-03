from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # sol1 O(n^2) time exceeded
        # ans = 0
        # for start in range(len(nums)):
        #     temp = 0
        #     for end in range(start, len(nums)):
        #         temp += nums[end]
        #         if temp == k:
        #             ans += 1
        # return ans
        
        # sol2 O(n) 435ms 21%
        hashMap = {0: 1}
        temp = 0
        ans = 0
        for num in nums:
            temp += num
            ans += hashMap.get(temp-k, 0)
            hashMap[temp] = hashMap.get(temp, 0) + 1
        return ans

print(Solution().subarraySum([1,1,1], 2))