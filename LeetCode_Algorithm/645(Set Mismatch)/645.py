from typing import List
'''
LeetCode 645 Set Mismatch

1~n까지 나열되어 있는 배열 중 미씽된 숫자와 중복된 숫자를 바꾸기

# sol1 T : 560ms 22% S : 15.3MB 85%
T : O(nlogn) S : O(logn)
소팅을 사용해서 정렬한 뒤 
이전 값과 현재 값을 비교하여 dup 값을 구한뒤
이전 값에 1을 더한 값이 현재 값이 더 작으면 그 값을 missing으로 넣는다.

# sol2 T : 227ms 89% S : 15.3MB 85%
T : O(n) S : O(1)
숫자를 루프로 돌려서 그 인덱스에 접근하여 해당하는 수를 -로 만들어
인덱스가 이전에 나타났는지 표시함. 나타났다면 dup에 저장
숫자를 돌려서 양수가 나오게 되면 missing 숫자로 간주하고 하나를 더한 값을 missing에 저장
'''
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # sol1
        # nums.sort(); ans = []; dup = -1; missing = 1
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i-1]:
        #         dup = nums[i]
        #     if nums[i-1] + 1 < nums[i]:
        #         missing = nums[i-1] +1
        # ans.append(dup)
        # if nums[len(nums)-1] != len(nums):
        #     ans.append(len(nums))
        # else:
        #     ans.append(missing)
        # return ans

        # sol2 
        dup = -1; missing = 1;
        for num in nums:
            if nums[abs(num)-1] < 0:
                dup = abs(num)
            else:
                nums[abs(num)-1] *= -1
        for i in range(1, len(nums)):
            if nums[i] > 0:
                missing = i + 1
        return [dup, missing]

print(Solution().findErrorNums([1,2,4]))
print(Solution().findErrorNums([3,2,2]))
print(Solution().findErrorNums([2,2]))

