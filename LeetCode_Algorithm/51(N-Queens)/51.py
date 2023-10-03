from turtle import back
from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # sol1 171ms 29%
        self.temp = [['.'] * n for _ in range(n)]
        self.ans = []
        self.dfs(0)
        return self.ans
    def dfs(self, r):
        if r == len(self.temp):
            temp = []
            for r in range(len(self.temp)):
                temp.append("".join(self.temp[r]))
            self.ans.append(temp); 
            return ;
        for c in range(len(self.temp[0])):
            if self.temp[r][c] != 'Q':
                self.temp[r][c] = 'Q'
                if self.Check(r-1, c):
                    self.dfs(r+1)
                self.temp[r][c] = '.'
    def Check(self, r,c):
        backslash = c-1; slash = c+1
        while -1 < r:
            if -1 < backslash and self.temp[r][backslash] == 'Q':
                return False
            if slash < len(self.temp[0]) and self.temp[r][slash] == 'Q':
                return False
            if self.temp[r][c] == 'Q':
                return False
            r -= 1; slash += 1; backslash -= 1
        return True
                
print(Solution().solveNQueens(4))
print(Solution().solveNQueens(5))
