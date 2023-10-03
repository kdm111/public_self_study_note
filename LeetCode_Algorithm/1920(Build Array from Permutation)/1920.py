'''
# sol1 129ms 65%
O(n) O(n)

# sol2 245ms 31% 14.1MB 86%
O(n) O(1)
해당 숫자에 접근하여 길이의 곱으로 만든 뒤
몫을 구한다.

'''
class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        # sol1
        # ans = []
        # for i in range(len(nums)):
        #     ans.append(nums[nums[i]])
        # return ans

        # sol2
        for i in range(len(nums)):
            if nums[i] < len(nums):
                nums[i] = nums[i] + len(nums) * (nums[nums[i]] % len(nums))
        for i in range(len(nums)):
            nums[i] //= len(nums)
        return nums