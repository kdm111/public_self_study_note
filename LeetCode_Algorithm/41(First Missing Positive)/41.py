'''
LeetCode 41 : First Missing Positive
정수 배열이 주어질 때 1부터 순서대로 존재하지 않는 최소의 숫자를 리턴하라

# sol1 276ms 85% 27.1MB 84%
O(n) O(n)
카운팅 배열을 사용해 배열에서 나타나는 인덱스에 체크한다.
배열이 가득 찬 경우 배열의 길이를 리턴한다.
'''
class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        # sol1
        for i in range(len(nums)):
            if nums[i] <= 0 or nums[i] > len(nums):
                nums[i] = 0
        mx = max(nums)
        arr = [0] * (mx + 1); arr[0] = 1
        for i in range(len(nums)):
            arr[nums[i]] = 1
        for i in range(len(arr)):
            if arr[i] == 0:
                return i
        return len(arr)

print(Solution().firstMissingPositive([1,2,3,4]))