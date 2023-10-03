from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # sol1 brute force O(2^n), O(n) time exceeded
    #     total_sum = sum(nums)
    #     # 만약 total_sum 이 홀수라면 그 숫자는 서브셋의 합으로 나타낼 수 없다.
    #     if total_sum % 2 == 1:
    #         return False
    #     return self.solve(tuple(nums), len(nums)-1, total_sum // 2)
    #     pass
    # def solve(self, nums, idx, rest_sum):
    #     # 남은 숫자의 합이 0일 경우 계산 완료
    #     if rest_sum == 0:
    #         return True
    #     # 배열의 끝까지 도달했거나 남은 rest_sum이 0보다 작음
    #     if idx == 0 or rest_sum < 0:
    #         return False
    #     # 하나씩 빼면서 점검하되 현재 위치하는 인덱스와 다를 수 있으므로 빼지 않고 진행한다.
        #return self.solve(nums, idx-1, rest_sum-nums[idx-1]) or self.solve(nums, idx-1, rest_sum)
        
        # sol2 dynamic programming
        # O(mn) O(n) 828ms 70%
        # 전체 합의 1/2만 존재하는 것이 확인 되면 됨
        # 셋에서 nums의 요소를 기존값과 함께 저장한 뒤로 값이 존재하는 지 체크
        # total_sum = sum(nums)
        # if total_sum % 2 == 1:
        #     return False
        # total_sum //= 2
        # # 체크 시간을 줄이기 위해 set 사용
        # lst = set([nums[0]])
        # for x in nums[1:]:
        #     for y in list(lst):
        #         lst.add(x+y)
        # print(lst)
        # return total_sum in lst

        # sol3 dynamic_programming O(mn) O(n) 1515ms 51%
        total_sum = sum(nums)
        if total_sum % 2: return False
        total_sum //= 2
        dp = [False for _ in range(total_sum+1)]
        dp[0] = True
        for curr in nums:
            for j in range(total_sum, curr-1, -1):
                # j는 j-curr이 true이면 true
                # 즉 curr 값은 항상 true가 된다.
                # 그리고 부분합은 항상 true이 된다.
                dp[j] = dp[j] or dp[j-curr]
        return dp[total_sum]
        
print(Solution().canPartition([1,5,11,5]))