from typing import List
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        # sol1 150ms 38%
        # mnlogmn 정렬에 걸리는 시간
        m = len(mat); n = len(mat[0]);
        for r in range(m):
            self.solve(mat, r, 0)
        for c in range(1, n):
            self.solve(mat, 0, c)
        return mat
    def solve(self, mat, r, c):
        m = len(mat); n = len(mat[0])
        i = r; j = c
        temp = []
        while i < m and j < n:
            temp.append(mat[i][j]);
            i, j = i+1, j+1
        temp.sort()
        i = 0;
        while r < m and c < n:
            mat[r][c] = temp[i]
            print(r,c,i)
            r,c,i = r+1, c+1, i+1
        
        

print(Solution().diagonalSort([[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]))