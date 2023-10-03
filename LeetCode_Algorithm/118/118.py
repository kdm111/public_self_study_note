from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        # sol1 O(numRows^2), O(numRows^2) 24~32ms 98~86%
        # ans = [[1]]
        # n = 1
        # while n < numRows:
        #     temp = [1]
        #     for i in range(len(ans[-1])-1):
        #         j = ans[-1][i]+ans[-1][i+1]
        #         temp.append(j)
        #     temp.append(1)
        #     ans.append(temp)
        #     n += 1
        # return ans

        # sol2 O(numRows^2), O(numRows^2)

        triangle = []
        for row_num in range(numRows):
            # 빈 공간 만들기
            row = [None for _ in range(row_num+1)]
            row[0], row[-1] = 1, 1

            for j in range(1, len(row)-1):
                row[j] = triangle[row_num-1][j-1] + triangle[row_num-1][j]
            triangle.append(row)
        return triangle

            

print(Solution().generate(5))