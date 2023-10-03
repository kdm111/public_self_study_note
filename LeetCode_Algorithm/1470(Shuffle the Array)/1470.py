'''
LeetCoe 1470 : shuffle the array
배열 셔플하기 [1,2,3,4] => [1,3,2,4]

# sol1 63ms 58% 14.1MB 31%
n을 기준으로 셔플을 해야 한다.
절반으로 나눠 뒤에 각각 뒤에 비트 시프트로 저장한다.
뒤의 절반으로 부터 값을 하나씩 읽어오면서 값을 저장한다.

# sol2 67ms 31% 14.2MB 31%
새로운 배열 만들기

'''
class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        # sol1
        for i in range(n, len(nums)):
            nums[i] = nums[i] << 10 | nums[i - n]
        i = 0
        for j in range(n, len(nums)):
            nums[i] = nums[j] & 1023
            nums[i+1] = nums[j] >> 10
            i += 2
        return nums
    
        # sol2
        # i = 0; j = n; ans = []
        # while j < len(nums):
        #     ans.append(nums[i])
        #     ans.append(nums[j])
        #     i += 1; j += 1
        # return ans

print(Solution().shuffle([0,1,2,3], 2))