'''
Leet 162 : 
peak 요소는 이웃한 요소보다 더 큰 요소를 말한다.
peck 요소의 인덱스를 구하라

# sol1 
중간에 두 개의 픽을 확인
두 개 중 더 큰 쪽으로 계속해서 이동하여 나눔
'''
class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        # sol1 54ms 43% 16.4MB 23%
        l, r = 0, len(nums)-1
        while l < r:
            m1 = (l + r) // 2
            m2 = m1 + 1
            if nums[m1] < nums[m2]:
                l = m1 + 1
            else:
                r = m1
        return l
print(Solution().findPeakElement([1,2,3,1]))
print(Solution().findPeakElement([1,3,2,1]))
print(Solution().findPeakElement([1,2]))
print(Solution().findPeakElement([1]))
print(Solution().findPeakElement([1,2,3,1,6,7,8,1]))


