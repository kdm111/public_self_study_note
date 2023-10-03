from typing import List
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # sol1 1616ms 5%
        # hashMap two pointer
        # O(n) O(n)
        # from collections import defaultdict
        # hashMap = defaultdict(list)
        # ans = left = right = 0;
        # while right < len(nums):
        #     hashMap[nums[right]].append(right)
        #     if len(hashMap[0]) == k+1:
        #         val = hashMap[0].pop(0)
        #         left = val+1
        #     ans = max(ans, right-left+1)
        #     right += 1
        # return ans


        # sol2 644ms 20% 17.18MB 43%
        # O(n) O(1)
        ans = left = right = 0;
        while right < len(nums):
            if nums[right] == 0:
                k -= 1
            while k < 0 and left < len(nums):
                if nums[left] == 0:
                    k += 1
                left += 1
            ans = max(ans, right-left+1)
            right += 1
        return ans

            
            
        pass

print(Solution().longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))
print(Solution().longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))
