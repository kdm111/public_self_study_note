from typing import List

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        # sol1 O(n), O(n) 96~145ms 76~27%
        # return solve(matrix, 0, 0)
        
        # sol2
        # group by category
        # diagonal은 r-c값이 일정하다.
        # 배열을 순회할 동안 
        groups = {}
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if r-c not in groups:
                    groups[r-c] = val
                elif groups[r-c] != val:
                    return False
        return True

# def solve(matrix, m, n):
#     i = m; j = n
#     prev = matrix[n][m]
#     i += 1; j += 1
    
#     while i < len(matrix[0]) and j < len(matrix):
#         curr = matrix[j][i]
#         print(f" prev : {prev} {j-1}{i-1}, curr : {curr} {j}{i}")
#         if prev != curr: return False
#         prev = curr
#         i += 1; j += 1

#     a, b = True, True
#     if m+1 < len(matrix[0]) and n == 0:
#         a = solve(matrix, m+1, n)
#     if n+1 < len(matrix) and m == 0:
#         b = solve(matrix, m,n+1)

#     return a and b
    
    

print(Solution().isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]]))