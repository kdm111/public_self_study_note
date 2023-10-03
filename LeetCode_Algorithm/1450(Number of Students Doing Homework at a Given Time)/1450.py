'''
LeetCode 1450 : Number of Students Doing Homework at a Given Time
주어진 k에 숙제를 하고 있는 학생의 숫자를 구하라.

# sol1 38ms 92% 13.9MB 74%
O(n) O(1)
주어진 숫자에 조건문을 사용해서 해결
'''
from typing import List
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        # sol1
        ans = 0
        for i in range(len(startTime)):
            if endTime[i] >= queryTime and queryTime >=startTime[i] and endTime[i] >= startTime[i]:
                ans += 1
        return ans
                