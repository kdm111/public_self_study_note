class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # sol1 685ms 29%
        # nums.sort()
        # l = 0; r = len(nums) -1; ans = 0
        # while l < r:
        #     temp = nums[l] + nums[r]
        #     if temp == k:
        #         l += 1; r -= 1; ans += 1
        #     elif temp > k:
        #         r -= 1;
        #     else:
        #         l += 1
        # return ans

        # sol2 628ms 93%
        counter = self.makeCounter(nums)
        ans = 0
        for num in counter:
            if k - num in counter:
                ans += min(counter[k], counter[num])
        return ans // 2


    def makeCounter(self, nums):
        counter = {}
        for num in nums:
            if num not in counter:
                counter[num] = 1
            else:
                counter[num] += 1
        return counter

