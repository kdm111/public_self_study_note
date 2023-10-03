'''
LeetCode 1235 : Maximum Profit in Job Scheduling
n개의 일이 있을 때 벌 수 있는 가장 많은 돈을 구하기

# sol1
일을 시작하면 끝날 때까지 다른 일을 할 수 없다.
일을 시작하고 끝날 때 일에 대한 반복문을 돌린다.

'''
from typing import List

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = []
        for i in range(len(startTime)):
            jobs.append([startTime[i], endTime[i], profit[i]])

        
