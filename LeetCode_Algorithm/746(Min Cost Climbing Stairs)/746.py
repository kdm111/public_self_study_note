from typing import List

'''
LeetCode 746 : Min Cost Climbing Stairs
계단을 오르기 위해서는 비용이 필요하다. 
계단은 한 번에 1개나 두 개가 올라갈 수 있다. 최소 비용을 구하라

# sol1
# O(n), O(n) 60ms 62% 14MB 32%
현재값과 이전의 두 값을 비교하여 최소값을 저장하면서 dp
'''
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # sol1 
        dp = [0 for _ in range(len(cost))]
        dp[0] = cost[0]; dp[1] = cost[1]
        
        for i in range(2, len(cost)):
            dp[i] = min(dp[i-2]+cost[i], dp[i-1]+cost[i])
        return min(dp[-2], dp[-1])


        # sol2
        # one = 0; two = 0;
        # for i in range(2, len(cost)+1):
        #     temp = one
        #     one = min(one + cost[i-1], two + cost[i-2])
        #     two = temp
        # return one
    

print(Solution().minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))