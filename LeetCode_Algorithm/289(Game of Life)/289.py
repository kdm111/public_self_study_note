'''
leetcode 289 : Game of Life

(0은 죽은 세포) (1은 살아있는 세포)
다음과 같은 조건에 따라 배열을 수정하라
1. 2개 미만의 살아있는 이웃을 가진 세포는 죽는다.
2. 2~3개의 살아있는 이웃을 가진 세포는 다음 세대로 이어진다.
3. 3개 초과하는 살아있는 이웃을 가진 세포는 과잉으로 죽는다.
4. 정확히 3개의 살아있는 이웃을 가진 세포는 재생성되어 살아난다.
'''
class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        # sol1 43ms 42% 16.2MB 98%
        dr = [-1, -1, 0, 1, 1, 1, 0, -1]
        dc = [0, 1, 1, 1, 0, -1, -1, -1]
        set_one = set()
        set_zero = set()
        for r in range(len(board)):
            for c in range(len(board[0])):
                cnt_1 = 0
                for k in range(8):
                    new_r, new_c = r + dr[k], c + dc[k]
                    if 0 <= new_r < len(board) and 0 <= new_c < len(board[0]):
                        if board[new_r][new_c] == 1:
                            cnt_1 += 1
                if (cnt_1 > 3 or cnt_1 < 2) and board[r][c] == 1:
                    set_zero.add((r,c))
                elif cnt_1 == 3 and board[r][c] == 0:
                    set_one.add((r,c))
        for (r,c) in set_one:
            board[r][c] = 1
        for (r,c) in set_zero:
            board[r][c] = 0

                
                        
        