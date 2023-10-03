'''
LeetCode : 36 Valid Sudoku
주어지는 스도쿠가 적합한 지 확인하는 문제
스도쿠는 반드시 해결될 필요가 없으며 주어진 숫자들이 정해진 규칙에만 따르는지 체크한다.
주어지는 스도쿠는 길이가 9*9이며 주어지는 크기는 1-9이다.

# sol1 T :  113ms 80% 14MB 36.8%
O(n^2) O(1)
주어진 숫자들만 세서 그 숫자들이 중복인지 반복문으로 체크한다.

'''
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # sol1
        self.board = board
        row, col = 0, 0
        while self.possibleCheck(row, col):
            col += 1
            if col == len(self.board[0]):
                row, col = row + 1, 0
            if row == len(self.board):
                return True
        return False
    
    def possibleCheck(self, row, col):
        if self.board[row][col] == '.':
            return True
        if self.rowCheck(row, col) and self.colCheck(row, col) and self.cubeCheck(row, col):
            return True
        return False

    def rowCheck(self, row, col):
        for c in range(len(self.board[0])):
            if c != col:
                if self.board[row][col] == self.board[row][c]:
                    return False
        return True

    def colCheck(self, row, col):
        for r in range(len(self.board[0])):
            if r != row:
                if self.board[row][col] == self.board[r][col]:
                    return False
        return True   
 
    def cubeCheck(self, row, col):
        cube_r, cube_c = row // 3 * 3, col // 3 * 3
        for c_r in range(cube_r, cube_r+3):
            for c_c in range(cube_c, cube_c+3):
                if c_r != row and c_c != col:
                    if self.board[row][col] == self.board[c_r][c_c]:
                        return False
        return True

                

print(Solution().isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))

# print(Solution().isValidSudoku([["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]))