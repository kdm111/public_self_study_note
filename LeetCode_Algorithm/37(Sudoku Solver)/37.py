
from typing import List
from zoneinfo import available_timezones
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        # 
        self.dfs(board, 0, 0)
    # 해당 row와 col에서 가능한 숫자들만 찾기
    def availableNumber(self, board, row, col):
        numSet= set()
        # 가로줄 확인
        for c in range(0, 9):
            if '0' <= board[row][c] <= '9':
                numSet.add(board[row][c])
        # 세로줄 확인
        for r in range(0, 9):
            if '0' <= board[r][col] <= '9':
                numSet.add(board[r][col])
        temp_r = (row // 3) * 3
        temp_c = (col // 3) * 3
        for r in range(temp_r,temp_r+3):
            for c in range(temp_c,temp_c+3):
                numSet.add(board[r][c])
        stack = [str(i) for i in range(1, 10)]
        ret = []
        for num in stack:
            if num not in numSet:
                ret.append(num)
        return ret
    
    def dfs(self, board, row, col):

        # sol1 330ms 60%
        # 빈 공간 찾기
        while board[row][col] != '.':
            col += 1
            if col == 9:
                col = 0; row = row+1
            if row == 9:
                return True
        # 해당 좌표에서 가능한 숫자 찾기
        stack = self.availableNumber(board,row,col)

        for num in stack:
            board[row][col] = num
            if self.dfs(board, row, col):
                return True
        board[row][col] = '.'
        return False
            
            
    
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
b = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Solution().solveSudoku(b)
Solution().solveSudoku(board)

print(board)
print(b)

            
                
                    