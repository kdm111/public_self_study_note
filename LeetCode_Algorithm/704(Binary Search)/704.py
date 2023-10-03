from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # sol1 350ms 43%보다 빠름
        # left = 0
        # right = len(nums)-1

        # while left <= right:
        #     mid = (left+right)//2
        #     if nums[mid] == target:
        #         return mid
            
        #     if nums[mid] < target:
        #         left = mid+1
        #     else:
        #         right = mid-1

        # return -1


        # sol2 250ms
        # left, right = 0, len(nums) - 1
        # while left <= right:
        #     pivot = left + (right - left) // 2
        #     print(left, right, pivot)
        #     if nums[pivot] == target:
        #         return pivot
        #     if target < nums[pivot]:
        #         right = pivot - 1
        #     else:
        #         left = pivot + 1
        # return -1

        # 왜 mid=(left+right)//2 보다 mid = left +(right-left)//2 가 더 나을 까?
        # https://ai.googleblog.com/2006/06/extra-extra-read-all-about-it-nearly.html
        # mid=(left+right)//2
        # 위의 경우에는 left+right가 최대 양수값 2^31-1q보다 크면 오버플로우되고 값이 음수로 되어 실패한다.
        # 그래서 mid = left + ((right-left)//2 로 바꾸면 된다.

        # sol3 243ms 68% 15.4MB 59%
        # python, js에서는 대체로 문제가 없고,
        # C, Java에서는 문제가 된다.
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1
    
        # sol3-1
        # 만약 중복이 있고 가장 왼쪽에 있는 인덱스를 찾아야 하는 경우
        # left, right = 0, len(nums)
        # while left < right:
        #     mid = (left + right) // 2
        #     if nums[mid] >= target:
        #         right = mid
        #     else:
        #         left = mid + 1
        # return left
    
        # sol3-2
        # 만약 중복이 있고 가장 오른쪽에 +1에 있는 인덱스를 찾아야 하는 경우
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        return left

            


print(Solution().search([-1,0,3,5,9,12],9))