from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # O(mn) O(mn) 48ms 51%
        # cpy = []
        # for r in range(len(matrix)):
        #     temp = []
        #     for c in range(len(matrix)):
        #         temp.append(matrix[r][c])
        #     cpy.append(temp)


        # for r in range(len(matrix)):
        #     for c in range(len(matrix)):
        #         matrix[r][c] = cpy[len(matrix) -c -1][r]

        # O(mn) O(1) 48ms 51%
        # transpose
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # reflect
        for i in range(len(matrix)):
            for j in range(len(matrix) // 2):
                matrix[i][j], matrix[i][-j-1] = matrix[i][-j-1], matrix[i][j]
        print(matrix)

        


print(Solution().rotate([[1,2,3],[4,5,6],[7,8,9]]))