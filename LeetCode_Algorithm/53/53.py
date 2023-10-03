import math
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # sol1 brute force n^3 시간초과

        # ans = -math.inf
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)+1):
        #         temp_nums = nums[i:j]
        #         temp_ans = 0
        #         for k in range(len(temp_nums)):
        #             temp_ans += temp_nums[k]
        #         if temp_ans > ans: ans = temp_ans        
        # return ans

        # sol2 최적화된 n^2 시간초과
        # ans = -math.inf
        # for i in range(len(nums)):
        #     temp_ans = 0
        #     for j in range(i, len(nums)):
        #         temp_ans += nums[j]
        #         if temp_ans > ans: ans = temp_ans
        # return ans

        # sol3 카데인 알고리즘 최소 660ms 99.5%보다 빠름. 최대 1500ms 
        # 중요한 부분은 배열이 어디서 부터 시작해야 하는 지 아는 것이다.
        # 직관적으로 앞에서 더해온 합이 다음 원소의 숫자보다 작다면 굳이 앞의 내용을 배열에 포함하지 않아도 된다.
        # 그냥 새로운 숫자부터 배열의 합을 계산해 가면 된다.
        
        # curr_sum_array는 앞에서 부터 계산해 나가면서 만약 새로 나오는 원소가 지금까지의 값보다 크면 새로 나오는 원소부터 배열을 시작한다.
        # ans는 최종적으로 나오는 답이며 현재까지 합한 값과 현재까지 나온 max값을 비교하여 저장한다.
        ans = 0
        curr_sum_array = 0
        for num in nums:
            temp = curr_sum_array+num
            curr_sum_array = num if temp < num else temp # curr_sum_array = max(num, temp)
            ans = curr_sum_array if ans < curr_sum_array else ans

        return ans

        pass
        

print(Solution().maxSubArray([5,4,-1,7,8]))