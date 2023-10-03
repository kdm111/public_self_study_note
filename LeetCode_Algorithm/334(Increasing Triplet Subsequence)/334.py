'''
문제에서는 3가지의 지금까지 나온 수 중에서 3가지만 작으면 된다.
first에는 가장 작은 수가 들어가고 second에는 두번째로 작은 수가 들어간다.
현재 위치한 숫자보다 과거에 더 작은 수가 2개만 발견되면 된다.
'''
class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        # 1057ms 75% 32.5MB 5%
        first = second = float('inf')
        for i in range(len(nums)):
            if nums[i] <= first:
                first = nums[i]
            elif nums[i] <= second:
                second = nums[i]
            else:
                return True
        return False

# print(Solution().increasingTriplet([1,2,3,4,5]))
# print(Solution().increasingTriplet([5,4,3,2,1]))
# print(Solution().increasingTriplet([2,1,5,0,4,6]))
# print(Solution().increasingTriplet([20,100,10,12,5,13]))
print(Solution().increasingTriplet([0,4,2,1,0,-1,-3]))

37 44 51 58 4 12 21 30







