'''
LeetCode 153 : Find Minimum in Rotated Sorted Array
주어진 배열은 오름차순으로 n의 길이만큼 회전되어 있다.
회전은 n-1, 0, 1 ... n-2, n-1, 0 ... 이렇게 이루어진다.
배열에서 최소값을 찾아라. 중복되는 값은 없다.

# sol1
left, right = 0, len(nums)-1
mid값이 right보다 더 작으면 mid..right까지는 오름차순으로 되어 있으므로 right을 mid로 옮김
중복되는 값은 없으므로 
mid값이 right보다 더 크면 left를 mid+1으로 이동
'''
class Solution:
    def findMin(self, nums: list[int]) -> int:
        # sol1
        left = 0; right = len(nums)-1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid+1
        return nums[left]
                
# print(Solution().findMin([3,1,2]))
# print(Solution().findMin([3,2,1]))

print(Solution().findMin([4,5,1,2]))
# print(Solution().findMin([4,5,6,7,0,1,2]))

