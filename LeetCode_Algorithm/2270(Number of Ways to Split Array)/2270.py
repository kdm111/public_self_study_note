class Solution:
    def waysToSplitArray(self, nums: list[int]) -> int:
        # sol1 996ms 67% 28.8MB 77%
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])
        ans = 0
        for i in range(len(prefix)-1):
            # left는 left까지의 합
            left = prefix[i]
            # right는 left를 제외한 합
            right = prefix[-1] - prefix[i]
            if left >= right:
                ans += 1
        return ans
print(Solution().waysToSplitArray([10,4,-8,7]))