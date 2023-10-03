'''
LeetCode 1493
배열에서 하나의 요소를 지우고 가장 긴 1의 개수
단 반드시 하나의 요소를 지워야 한다.

# sol1 393ms 51% 18.9MB 46%
l,r을 진행시키면서 
'''
class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        # sol1 
        if len(set(nums)) == 1:
            return len(nums) - 1 if nums[0] == 1 else 0
        l, r, cnt0 = 0, 0, 0
        ans = 0
        while r < len(nums):
            if nums[r] == 0:
                cnt0 += 1
            while cnt0 == 2:
                if nums[l] == 0:
                    cnt0 -= 1
                l += 1
            ans = max(ans, r-l)
            r += 1
        return ans
    
print(Solution().longestSubarray([0,1,1,1,0,1,1,0,1]))
print(Solution().longestSubarray([1,1,1]))
print(Solution().longestSubarray([1,1,1,0]))
print(Solution().longestSubarray([1,1,1,0,1]))



            
                
                    
                    
                    
                    
                    
            
        