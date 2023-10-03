from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # sol1 O(n^2) time exceedded
        # ans = 0
        # for i in range(len(height)):
        #     for j in range(i, len(height)):
        #        temp = (j - i) * min(height[i], height[j])
        #        if ans < temp:
        #            ans = temp
        # return ans

        # sol2 O(n) 959ms 49%
        i, j = 0, len(height)-1
        ans = 0
        while i < j:
            temp = (j - i) * min(height[i], height[j])
            if ans < temp:
                ans = temp
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return ans

print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))