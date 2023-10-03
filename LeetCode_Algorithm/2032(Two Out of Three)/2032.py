'''
LeetCode 2032 : Two Out of Three
세 배열에서 두 배열에 겹치는 요소들을 반환하라

# sol1
각 배열의 세트 값을 and와 or로 연결한다.

'''
class Solution:
    def twoOutOfThree(self, nums1: list[int], nums2: list[int], nums3: list[int]) -> list[int]:
        return set(nums1) & set(nums2) | set(nums2) & set(nums3) | set(nums3) & set(nums1)