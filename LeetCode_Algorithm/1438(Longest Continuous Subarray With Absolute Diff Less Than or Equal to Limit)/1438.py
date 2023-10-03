'''
LeetCode 1438 : Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit

# sol1 1358ms 21% 23MB 66%
서브 배열안에서 최대값과 최소값을 가지고 있어야 하므로
inc와 dec를 가지고 inc는 최소값부터 시작해서 계산한뒤 
dec는 최대값부터 내려오는 배열을 갖게 된다.
inc와 dec가 limit보다 커진다면 left의 값과 일치하는 값을 제거한다.


'''
class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        ans = 0; inc = []; dec = []
        left = 0
        for right, num in enumerate(nums):
            while inc and inc[-1] > num:
                inc.pop()
            while dec and dec[-1] < num:
                dec.pop()
            inc.append(num)
            dec.append(num)
            while inc and dec and dec[0] - inc[0] > limit:
                if nums[left] == dec[0]:
                    dec.pop(0)
                if nums[left] == inc[0]:
                    inc.pop(0)
                left += 1
            ans = max(ans, right-left+1)
        return ans

print(Solution().longestSubarray([8,2,4,7], 4))
print(Solution().longestSubarray([10,1,2,4,7,2], 5))
print(Solution().longestSubarray([4,2,2,2,4,4,2,2], 0))

