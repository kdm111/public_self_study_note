from typing import List

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        # O(n) 22ms 99.52%
        # if nums == []:
        #     if upper - lower == 0:
        #         return [f"{lower}"]
        #     elif abs(upper - lower) >= 1:
        #         return [f"{lower}->{upper}"]

        # ans = []
        # if abs(nums[0] - lower) == 1:
        #     ans.append(f"{lower}")
        # elif abs(nums[0] - lower) > 1:
        #     ans.append(f"{lower}->{nums[0]-1}")

        # temp = []
        # for i in range(len(nums)-1):
        #     temp.append([nums[i], nums[i+1]])
        # print(ans, temp)
        # for i,j in temp:
        #     if abs(j - i) <= 1:
        #         continue
        #     elif abs(j - i) == 2:
        #         ans.append(f'{i+1}')
        #     else:
        #         ans.append(f"{i+1}->{j-1}")

        # if abs(upper - nums[-1]) == 1:
        #     ans.append(f"{upper}")
        # elif abs(upper - nums[-1]) > 1:
        #     ans.append(f"{nums[-1]+1}->{upper}")

        # return ans

        # O(n) O(1) 51ms 23%
        ans = []
        def check(low, curr):
            if low == curr:
                return f"{low}"
            return f"{low}->{curr}"

        low = lower - 1
        for i in range(len(nums)+1):
            curr = nums[i] if i < len(nums) else upper + 1
            if low + 1 <= curr - 1:
                ans.append(check(low+1, curr-1))
            low = curr
        return ans


# print(Solution().findMissingRanges([0,1,3,50,75], 0, 99))
# print(Solution().findMissingRanges([-1], -1, -1))
# print(Solution().findMissingRanges([1], 1, 1))
# print(Solution().findMissingRanges([-1], -2, -1))
print(Solution().findMissingRanges([2], 0, 9))



# print(Solution().findMissingRanges([], 0, 3))
# print(Solution().findMissingRanges([4,5], 4, 5))
# print(Solution().findMissingRanges([1,3,5], 1, 5))



