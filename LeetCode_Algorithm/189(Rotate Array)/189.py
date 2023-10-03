from tkinter import N
from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # sol1 time limit exceeded
        # O(kn) O(1)
        # while k > 0:
        #     temp = nums[-1]
        #     for n in range(len(nums)-1, 0, -1):
        #         nums[n] = nums[n-1]
        #     nums[0] = temp
        #     k -= 1

        # sol2
        # O(n) O(n)
        # 임시로 만들어 놓고 O(n)으로 이동한 뒤
        # nums에 복사
        # temp = [0] * len(nums)
        # for i in range(len(nums)):
        #     temp[(i+k)%len(nums)] = nums[i]
        # nums[:] = temp

        # sol3 578ms 29%
        # O(n) O(1)
        # n = len(nums)
        # k %= len(nums)
        # nums[:] = nums[n-k:] + nums[:n-k]
        # return nums

        # sol4 779ms 25%
        # O(n) O(1)
        # 숫자를 결정한 뒤 알맞은 위치에 넣고 그 위치에 있는 값은 따로 저장한다.
        n = len(nums)
        k %= n
        start = cnt = 0
        # 정해진 교환이 다 일어나면 종료
        while cnt < n:
            # 현재 위치 값과 해당 값을 저장
            curr, temp = start, nums[start]
            while True:
                # 다음 인덱스를 찾음
                next_idx = (curr+k) % n
                # 알맞은 위치에 넣음
                temp, nums[next_idx] = nums[next_idx], temp
                cnt += 1
                curr = next_idx
                if start == curr:
                    break
            start += 1
            
        



print(Solution().rotate([1,2,3,4,5,6], 2))
# print(Solution().rotate([1], 3))
# print(Solution().rotate([1,2], 1))

