from typing import List

class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:

        # O(n), O(n) 65ms 38%
        lst = [0] * 2051
        for log in logs:
            for year in range(log[0], log[1]):
                lst[year] += 1
        return lst.index(max(lst))

print(Solution().maximumPopulation([[1993,1999],[2000,2010]]))