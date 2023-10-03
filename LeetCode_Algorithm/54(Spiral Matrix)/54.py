from locale import currency
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # sol1 O(mn) O(1) 29ms 96%
        m = len(matrix); n = len(matrix[0])
        r = 0; c = 0;
        dr = [0,1,0,-1]
        dc = [1,0,-1,0]
        visited = True
        ans = [matrix[0][0]]
        matrix[0][0] = visited
        current_dir = -1
        while len(ans) != m*n:
            current_dir = (current_dir+1) % 4
            while True:
                r += dr[current_dir]; c += dc[current_dir]
                if not (0 <= r < m and 0 <= c < n):
                    r -= dr[current_dir]; c -= dc[current_dir]
                    break
                if matrix[r][c] == visited:
                    r -= dr[current_dir]; c -= dc[current_dir]
                    break
                ans.append(matrix[r][c])
                matrix[r][c] = visited
        return ans
                
        pass



print(Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(Solution().spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
print(Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9],[10,11,12]]))

