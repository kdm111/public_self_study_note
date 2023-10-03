'''
LeetCode 2444 : Count Subarrays With Fixed Bounds
주어진 배열에서 하위 배열을 구하는 데 하위 배열의 min값이 minK이고 max값이 maxK인 하위 배열의 개수를 구하라.

# sol1
배열을 순회하면서 시작점과 마지막으로 나타난 minK, maxK값을 저장한다.
각 반복이 끝날 때 [start + 1, min(minIdx, maxIdx)]를 더한다.

'''
class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        minIdx = -1; maxIdx = -1
        start = -1; ans = 0
        for i in range(len(nums)):
            if nums[i] < minK or nums[i] > maxK:
                start = i
            if nums[i] == minK:
                minIdx = i
            if nums[i] == maxK:
                maxIdx = i
            ans += max(0, min(maxIdx, minIdx)-start)
        return ans
print(Solution().countSubarrays([1,3,5,2,7,5], 1, 5))
# print(Solution().countSubarrays([1,1,1,1], 1, 1))
