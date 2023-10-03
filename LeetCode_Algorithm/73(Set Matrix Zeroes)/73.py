'''
LeetCode 73 : Set Matrix Zeroes
처음 0주위의 상하좌우 모두 0으로 바꿔라

# sol1
0인 인덱스를 모아서 그 가로 세로줄을 모두 0으로 초기화
O(m*n) O(n)


'''
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        # sol1
        zero = []
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    zero.append((r,c))
        for r,c in zero:
            self.setZero(r,c,matrix)

                    
                        
    def setZero(self, r, c, matrix):
        dr = [0,1,0,-1]
        dc = [1,0,-1,0]
        for i in range(4):
            newR = r+dr[i]; newC = c+dc[i]
            while 0 <= newR < len(matrix) and 0 <= newC < len(matrix[0]):
                matrix[newR][newC] = 0
                newR += dr[i]; newC += dc[i]
            
'''
1 1 1
1 0 1
1 1 1

'''
            
            
        
print(Solution().setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))