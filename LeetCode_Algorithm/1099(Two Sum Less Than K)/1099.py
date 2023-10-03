from typing import List

''''
LeetCode : 1099 Two Sum Less Than K
숫자들의 배열이 들어올 때 두 숫자의 합이 k보다 작은 최대의 수를 구하라
만약 더 작은 숫자를 만들지 못한다면 -1을 리턴해라.

# sol1 83ms 64% 13.9MB 72%
정렬에 필요한 복잡도 : O(nlogn) O(logn)~O(n)
들어오는 어레이를 정렬한 뒤 투 포인터를 사용해서 최대값을 구한다.

# sol2 63ms 81% 13.9MB 72%
O(m+n) O(n)
카운팅 소트 사용
카운팅 소트를 사용해서 정렬에 필요한 시간복잡도를 줄이고 인덱스를 투 포인터로 조절하면서
문제를 해결한다.
단 숫자는 중복이 허용되므로 주의해야 한다.
'''
class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        # sol1
        # nums.sort()
        # left, right = 0, len(nums)-1
        # ans = -1
        # while left < right:
        #     temp = nums[left] + nums[right]
        #     if temp < k:
        #         if ans <= temp:
        #             ans = temp; 
        #         left += 1
        #     else:
        #         right -= 1
        # return ans

        # sol2
        cntArr = [0] * 1001
        ans = -1
        for num in nums:
            cntArr[num] += 1
        left, right = 0, len(cntArr)-1
        while left <= right:
            if left + right >= k or cntArr[right] == 0:
                right -= 1
            else:
                if cntArr[left] > (0 if left < right else 1):
                    ans = max(ans, left+right)
                left += 1
        return ans
        
        

print(Solution().twoSumLessThanK([34,23,1,24,75,33,54,8], 60))