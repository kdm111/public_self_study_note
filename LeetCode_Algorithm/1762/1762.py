from typing import List

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        # sol1 O(n) 927~1231ms 55~21%
        # max_height = heights[-1]
        # ans = [len(heights)-1]
        # for idx in range(len(heights)-1, -1, -1):
        #     if heights[idx] > max_height:
        #         max_height = heights[idx]
        #         ans.append(idx)

        # return ans[::-1]

        # sol2 O(n) 915ms 56%
        stack = [heights[0]]
        ans = [0]
        for idx in range(1, len(heights)):
            while stack and heights[idx] >= stack[-1]:
                stack.pop()
                ans.pop()
            stack.append(heights[idx])
            ans.append(idx)
        return ans
print(Solution().findBuildings([4,3,2,1]))
# print(Solution().findBuildings([4,2,3,1]))
# print(Solution().findBuildings([1,3,2,4]))

