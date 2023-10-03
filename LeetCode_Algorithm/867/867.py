from typing import List

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # O(mn) 87ms 63%
        m = len(matrix)
        n = len(matrix[0])
        ans = []
        for c in range(n):
            temp = []
            for r in range(m):
                temp.append(matrix[r][c])
            ans.append(temp)
        return ans
        pass

print(Solution().transpose([[1,2,3],[4,5,6]]))