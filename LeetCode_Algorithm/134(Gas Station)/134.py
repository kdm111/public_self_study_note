from typing import List 

'''
LeetCode 134 : Gas Station

# sol2 722ms 72% 19.3MB 49%
O(n) O(1)
지금까지 온 거리가 만약 가스로 올 수 있는 거리라면 다시 돌아가 계산할 필요가 없다.
따라서 현재 가스가 0보다 작다면 다시 0으로 리셋하여 계산한다.


'''
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # sol1 O(n^2) time exceeded
        # for start in range(len(gas)):
        #     if gas[start] >= cost[start]:
        #         tank = gas[start] - cost[start]
        #         i = start + 1
        #         while True:
        #             if i >= len(gas): i = 0
        #             if start == i or tank < 0: break
        #             tank += gas[i] - cost[i]
        #             i += 1
        #         if tank >= 0:
        #             return start
        # return -1

        # sol2 O(n) 800ms 59%
        total_gas, curr_gas = 0, 0
        ans = 0
        for point in range(len(gas)):
            total_gas += gas[point] - cost[point]
            curr_gas += gas[point] - cost[point]
            if curr_gas < 0:
                curr_gas = 0
                ans = point + 1
        if total_gas >= 0: return ans
        else: return -1



print(Solution().canCompleteCircuit([3,1,1], [1,2,2]))