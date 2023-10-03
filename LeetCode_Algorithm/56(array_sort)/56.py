from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sol1 O(nlogn) 218ms 36%
        intervals.sort(key=lambda x : x[0])
        ans = []
        for interval in intervals:
            if ans == [] or ans[-1][1] < interval[0]:
                ans.append(interval)
            else:
                ans[-1][1] = max(ans[-1][1], interval[1])
        return ans
            

# print(Solution().merge([[1,3],[2,6],[8,10],[15,18]]))
# print(Solution().merge([[1,4],[0,4]]))
# print(Solution().merge([[1,4],[0,0]]))
# print(Solution().merge([[2,3],[4,5],[6,7],[8,9],[1,10]]))
# print(Solution().merge([[1,4], [1,4]]))
print(Solution().merge([[1,4], [2,3]]))




