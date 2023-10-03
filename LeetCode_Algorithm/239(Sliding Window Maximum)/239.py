from sys import maxsize
from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # sol1 time limit exceeded
        # O(nk) O(k)
        # left = 0; right = k-1
        # ans = []; 
        # while right < len(nums):
        #     ans.append(max(nums[left:right+1]))
        #     left += 1; right += 1
        # return ans

        # sol2 4143ms 10%
        # O(n) O(n)
        if len(nums) * k == 0:
            return []
        if k == 1:
            return nums
        ans = []
        from collections import deque
        queue = deque()
        for i,num in enumerate(nums):
            while queue and nums[queue[-1]] < num:
                queue.pop()
            queue.append(i)
            # 배열의 min_idx가 현재 속한 배열에서 빠져야 하는 인덱스라면
            if queue[0] == i-k:
                queue.popleft()
            # 배열에 담기기 위한 최소 인덱스 조건
            if i >= k-1:
                ans.append(nums[queue[0]])
        return ans


# print(Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
print(Solution().maxSlidingWindow([7,2,4], 2))
