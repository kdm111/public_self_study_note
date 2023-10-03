from typing import List
class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        # sol1 time exceeded limit
        # 일반 bfs O(mn) O(1)
        # self.dr = [0, 1, 0, -1]; self.dc = [1, 0, -1, 0]
        # self.ans = []
        # self.bfs(mat,0,0,0)
        # return self.ans[0]

        # sol2 
        # binary search
        start_col = 0; end_col = len(mat[0])
        while start_col <= end_col:
            checkLeft, checkRight = False, False
            mid_col = (start_col+end_col) // 2
            for row in range(len(mat)):
                if row > 0 and mat[row-1][mid_col] >= mat[row][mid_col]:
                    continue
                if row+1 < len(mat) and mat[row+1][mid_col] >= mat[row][mid_col]:
                    continue
                if mid_col+1 < len(mat[0]) and mat[row][mid_col+1] >= mat[row][mid_col]:
                    checkRight = True; continue
                if mid_col-1 >= 0 and mat[row][mid_col-1] >= mat[row][mid_col-1]:
                    checkLeft = True; continue
                return [row, mid_col]
            if checkLeft:
                end_col = mid_col-1
            else:
                start_col = mid_col+1
        return []
                
    def bfs(self,mat,r,c, cnt):
        flag = False
        for i in range(4):
            new_r = r+self.dr[i]
            new_c = c+self.dc[i]
            if 0 <= new_r < len(mat) and 0 <= new_c < len(mat[0]):
                if mat[new_r][new_c] > mat[r][c]:
                    flag = True
                    self.bfs(mat, new_r, new_c, cnt+1)
        if flag == False:
            self.ans.append([r,c])
                

print(Solution().findPeakGrid([[41,8,2,48,18],[16,15,9,7,44],[48,35,6,38,28],[3,2,14,15,33],[39,36,13,46,42]]))
print(Solution().findPeakGrid([[1,4],[3,2]]))
