class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        # sol1 1362ms 74% 33.9MB 96%
        if k >= len(nums) or k + k + 1 > len(nums):
            return [-1] * len(nums)
        ans = [-1] * len(nums)
        temp = 0; i = 0
        while i < len(nums) and i <= k:
            temp += nums[i]; i += 1
        j = k  + 1
        while j < len(nums) and j < k + k + 1:
            temp += nums[j]; j += 1
        
        l = k + k + 1
        ans[k] = int(temp / l); 
        i = 0; j = k + k + 1;
        k += 1;
        while j < len(nums):
            temp -= nums[i]; temp += nums[j]; 
            i += 1; j += 1
            ans[k] = int(temp / l); k += 1
        return ans

            

print(Solution().getAverages([7,4,3,9,1,8,5,2,6], 3))
print(Solution().getAverages([1000], 0))
print(Solution().getAverages([10], 10))
print(Solution().getAverages([1,11,17,21,29], 4))



#  0 1 2 3 4 5 6 7 8
# [7,4,3,9,1,8,5,2,6]