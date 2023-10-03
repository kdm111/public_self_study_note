from typing import List

from numpy import tri

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # 31ms 90%
        triangle = [[1], [1,1]]
        if rowIndex <= 1:
            return triangle[rowIndex]
        n = 1
        while n < rowIndex:
            temp = [1]
            for idx in range(len(triangle[n])-1):
                num = triangle[n][idx] + triangle[n][idx+1]
                temp.append(num)
            temp.append(1)
            triangle.append(temp)
            n += 1
        return triangle[rowIndex]
            

print(Solution().getRow(5))