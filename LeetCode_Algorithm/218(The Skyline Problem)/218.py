from typing import List
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        heights = [0] * (buildings[-1][0] + buildings[-1][1])
        ans = []
        for building in buildings:
            for r in range(building[0], building[1]+1):
                heights[r] = max(heights[r], building[2]);
        print(heights)
        i = 1;
        while i < len(heights)-1:
            if heights[i] != 0 and heights[i] != heights[i-1]:
                ans.append([i, heights[i]])
            i += 1
        if heights[i] != heights[i-1]:
            ans.append([i, heights[i]])
        return ans    
  
print(Solution().getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]))