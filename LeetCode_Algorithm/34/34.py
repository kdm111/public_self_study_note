from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # O(n) sol1 149ms 21%
        # ans = [-1, -1]
        # for idx, num in enumerate(nums):
        #     if num == target:
        #         if ans[0] != -1:
        #             ans[1] = idx
        #         else:
        #             ans[0] = idx; ans[1] = idx
        # return ans

        # O(logn) 122ms 42%
        ans = [-1, -1]
        start, end = 0, len(nums)-1
        while start <= end:
            mid = (start+end) // 2
            print(start, mid, end)
            if nums[mid] == target:
                if ans[0] == -1:
                    if mid == start or nums[mid-1] < target:
                        ans[0] = mid
                        start = 0; end = len(nums)-1
                        continue;
                    else:
                        end = mid - 1
                else:
                    if mid == end or nums[mid+1] > target:
                        ans[1] = mid
                        break
                    else:
                        start = mid + 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return ans


        # O(n)으로 해결할 수도 있지만 O(logn)으로 해결할 수 있음

print(Solution().searchRange([1,2,2,3,4,4,4], 4))