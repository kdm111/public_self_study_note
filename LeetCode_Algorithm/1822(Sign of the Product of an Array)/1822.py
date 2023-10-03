class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # sol1 45ms 54% 13.3MB 90%
        ans = 1
        for num in nums:
            if num == 0:
                return 0
            elif num < 0:
                ans *= -1
        return ans