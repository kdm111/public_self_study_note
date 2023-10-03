class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        # python3 set간의 연산
        return [list(set(nums1) - set(nums2)), list(set(nums2) - set(nums1))]