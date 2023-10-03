from typing import List

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        # sol1 O(n), O(1) 36~50ms 81~43%
        ans = 10000000000000000
        temp = -1
        for num in nums:
            temp += num
            if ans > temp: ans = temp
        return 1 if ans >= 0 else abs(ans)

print(Solution().minStartValue([-3,2,-3,4,2]))