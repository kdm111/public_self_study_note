'''
LeetCode 240 : Search a 2D Matrix II
2d 배열에서 목표하는 값이 있는지 검사하라

# sol1 177ms 80% 20.3MB 83%
O(n) O(1)
왼쪽 끝에서 시작하여 더 작으면 c을 증가시키고 작으면 r을 감소시킨다.

'''
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        # sol1
        if not matrix:
            return False
        r = len(matrix)-1; c = 0
        while r >= 0 and c < len(matrix[0]):
            if matrix[r][c] < target:
                c += 1
            elif matrix[r][c] == target:
                return True
            else:
                r -= 1
        return False

        
        
        

print(Solution().searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5))
# print(Solution().searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20))
print(Solution().searchMatrix([[1,4],[2,5]], 5))



