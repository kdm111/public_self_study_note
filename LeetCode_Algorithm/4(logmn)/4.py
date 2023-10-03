from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # sol1 O(n) 174ms 24%
        nums1_i = 0; nums2_i = 0
        merged_arr = []
        while nums1_i < len(nums1) and nums2_i < len(nums2):
            if nums1[nums1_i] < nums2[nums2_i]:
                merged_arr.append(nums1[nums1_i]); nums1_i += 1
            else:
                merged_arr.append(nums2[nums2_i]); nums2_i += 1
        if nums1_i < len(nums1):
            while nums1_i < len(nums1):
                merged_arr.append(nums1[nums1_i]); nums1_i += 1
        else:
            while nums2_i < len(nums2):
                merged_arr.append(nums2[nums2_i]); nums2_i += 1

        mid = len(merged_arr) // 2
        if len(merged_arr) % 2 == 0:
            return (merged_arr[mid] + merged_arr[mid-1]) / 2
        else:
            return merged_arr[mid]


# print(Solution().findMedianSortedArrays([1,2,3,4,5,6], [7,8,9,10,11,12,13]))
# print(Solution().findMedianSortedArrays([2], [3,4]))
# print(Solution().findMedianSortedArrays([], [2,3]))


