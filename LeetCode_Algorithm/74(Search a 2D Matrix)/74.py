from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # sol1 greedy O(mn) O(1) 66ms 55%
        # for r in range(len(matrix)):
        #     for c in range(len(matrix[0])):
        #         if matrix[r][c] == target:
        #             return True
        # return False

        # sol2 binary search
        # log(mn) O(1) 50ms 85%
        # 행렬은 정렬되어 있음
        # 그리고 행렬은 0~r*c-1까지의 리스트로 볼 수 있다.
        # r = num // len(c) c = num % len(c)
        # r과 c의 값을 구분해서 이진 탐색으로 찾기
        left = 0; right = (len(matrix) * len(matrix[0])) - 1
        while left <= right:
            mid = left + (right-left // 2)
            r = mid // len(matrix[0])
            c = mid % len(matrix[0])
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                left = mid+1
            else:
                right = mid-1
        return False


print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))
