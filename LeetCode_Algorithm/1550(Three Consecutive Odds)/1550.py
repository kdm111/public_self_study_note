'''
LeetCode 1550 : Three Consecutive Odds
주어진 배열에서 홀수가 연속으로 3개 이상 존재하면 True를 반환하라

# sol1 57ms 80% 13.8MB 94%

'''
from typing import List
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        cnt = 0
        for num in arr:
            if num % 2:
                cnt += 1
            else:
                cnt = 0
            if cnt == 3:
                return True
        return False
            
        pass