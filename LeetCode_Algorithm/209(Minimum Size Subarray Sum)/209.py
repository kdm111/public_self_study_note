class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        # sol1 time limit exceeded 
        # import sys
        # i = 0; ans = sys.maxsize
        # for j in range(len(nums)+1):
        #     while sum(nums[i:j]) >= target:
        #         if sum(nums[i:j]) >= target:
        #             ans = min(ans, j-i)
        #         i += 1
            
        # return 0 if ans == sys.maxsize else ans

        # sol2 264ms 59% 29MB 40%
        import sys
        ans = sys.maxsize
        total = 0; i = 0
        for j in range(len(nums)):
            total += nums[j]
            while total >= target:
                ans = min(ans, j-i+1)
                total -= nums[i]
                i += 1
        return 0 if ans == sys.maxsize else ans
        
        

print(Solution().minSubArrayLen(7, [2,3,1,2,4,3]))
print(Solution().minSubArrayLen(99, [2,3,1,2,4,3,98,1,99]))
print(Solution().minSubArrayLen(4, [1,4,4]))
print(Solution().minSubArrayLen(11, [1,1,1,1,1,1,1,1]))
print(Solution().minSubArrayLen(11, [1,2,3,4,5]))






