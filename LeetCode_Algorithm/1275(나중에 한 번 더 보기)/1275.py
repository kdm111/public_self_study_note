from typing import List

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        # sol1 O(mn) O(n^2) 45~52ms 57~38%
        # m은 input의 길이 n은 보드의 가로 길이
        # board에 다 넣고 dfs로 찾기
#         global board
#         board =  [[None for _ in range(3)] for _ in range(3)]

#         for i in range(len(moves)):
#             chr = "A" if i % 2==0 else "B"
#             r,c = moves[i]
#             board[r][c] = chr

#         for r in range(3):
#             for c in range(3):
#                 if board[r][c] != None:
#                     ans = findWinner(r,c)
#                     if ans is not None:
#                         return ans
#         return "Draw" if len(moves) == 9 else "Pending"


# def findWinner(r,c):

#     chr = board[r][c]
#     dr = [0,1,0,-1,-1,1,1,-1]
#     dc = [1,0,-1,0,1,1,-1,-1]
#     cnt = 1

#     for i in range(8):
#         r2, c2, cnt2 = r +dr[i], c + dc[i], cnt
#         while  0 <= r2 < 3 and 0 <= c2 < 3:
#             if board[r2][c2] == chr:
#                 cnt2 += 1
#                 if cnt2 == 3:
#                     return board[r2][c2]
#                 r2 += dr[i]; c2 += dc[i]
#             else:
#                 break

        pass



        


    
        


    
 

print(Solution().tictactoe([[0,0],[1,1]]))