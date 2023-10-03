'''
LeetCode 45 : Jump Game II

# sol1 133ms 87% 15.1MB 56%
O(n) O(1)
현재 위치에서 가장 멀리 뛸 수 있는 거리를 재면서
현재 도달할 수 없는 거리라면 점프를 한 뒤 현재 도달할 수 있는 가장 긴 거리를 저장한다.

'''
class Solution:
    def jump(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 0
        ans = 0; far = 0; canJump = 0
        for i in range(len(nums)):
            if i > canJump:
                ans += 1
                canJump = far
            far = max(far, i+nums[i])
        return ans
        
        