from typing import List

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        # sol1 422ms 54%
        # O(n) O(1)
        # 먼저 배열이 존재할 때 각각 없는 숫자를 계산할 수 있다.
        # 1 4 10일경우
        # 1 2 3을 빼면
        # 0 2 7라는 결과를 만들 수 있다.
        # 위의 배열은 nums[idx]까지의 없어진 숫자를 의미한다.
        # k값이 각각 배열의 크기와 비교하여 더 작을 경우에 
        # 이전의 값에서 + k - idx를 하면 값이 나오게 된다.

        idx = 1
        while idx < len(nums) and self.missing(nums, idx) < k:
            idx += 1
        return nums[idx-1] + k - self.missing(nums, idx-1)
    def missing(self, nums, idx):
        return nums[idx] - (nums[0]+idx)



# 1 4 10
# 1 2  3
# 0 2  7
print(Solution().missingElement([4,7,9,10], 1))
print(Solution().missingElement([1,2,3,4], 10))
print(Solution().missingElement([1,4,10], 5))
print(Solution().missingElement([1,5,10], 2))


