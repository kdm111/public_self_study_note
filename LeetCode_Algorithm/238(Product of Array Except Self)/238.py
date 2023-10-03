'''
LeetCode 238 : Product of Array Except Self
정수 배열이 주어질 때 정수 배열을 반환하라. 
각 요소는 해당하는 위치의 idx를 제외한 모든 곱과 같다.

# sol1 239ms 65% 20.7MB 99%
O(n) O(1)
0의 개수와 0이 아닌 모든 곱을 구한다.
그 뒤에 배열을 순회하며 조건을 구분하여 값을 넣는다.

# sol2 219ms 95% 23.4MB 5.4%
O(n) O(n)
알고보니 나누기 연산을 하면 안된다.
일단 prefixProduct로 계속해서 곱해가며 자신의 왼쪽 까지의 모든 곱을 넣는다.
그 후 오른쪽부터 하나씩 곱해가면서 나머지를 곱한다.

'''
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # sol1
        # totalProduct = 1; zeroCnt = 0
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         zeroCnt += 1; continue
        #     totalProduct *= nums[i]
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         nums[i] = totalProduct if zeroCnt == 1 else 0
        #     else:
        #         nums[i] = int(totalProduct / nums[i]) if zeroCnt == 0 else 0
        # return nums

        # sol2
        length = len(nums)
        ans = [1] * length
        prefixProduct = 1
        for i in range(1, length):
            ans[i] = prefixProduct * nums[i - 1]
            prefixProduct *= nums[i - 1]

        prefixProduct = 1
        for i in range(length-1, -1, -1):
            ans[i] *= prefixProduct
            prefixProduct *= nums[i]
        return ans

print(Solution().productExceptSelf([2,3,0,0]))
print(Solution().productExceptSelf([0,1,2]))
print(Solution().productExceptSelf([1,2,3]))

# 1 2 3 4 5 6
# 1 1 1 1 1 1 
