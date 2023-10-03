import enum
from multiprocessing.managers import DictProxy
import sys
from typing import List
class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        # sol1 time limit exceeded
        # O(mn) O(1)
        # import sys
        # ans = []
        # for [idx, color] in queries:
        #     self.temp = sys.maxsize
        #     self.solve(idx, colors, color)
        #     if self.temp == sys.maxsize:
        #         ans.append(-1)
        #     else:
        #         ans.append(self.temp)
        # return ans

        # sol2 time limit exceeded
        # hashMap+O(n)
        # O(mn) O(n)
        # hashMap = {}; ans = []
        # for idx, color in enumerate(colors):
        #     if color in hashMap:
        #         hashMap[color].append(idx)
        #     else:
        #         hashMap[color] = [idx]

        # for [idx, color] in queries:
        #     if color not in hashMap:
        #         ans.append(-1); continue
        #     if idx <= hashMap[color][0]:
        #         ans.append(hashMap[color][0]-idx)
        #     elif idx >= hashMap[color][-1]:
        #         ans.append(idx-hashMap[color][-1])
        #     else:
        #         for loc in range(1, len(hashMap[color])):
        #             if hashMap[color][loc-1] <= idx <= hashMap[color][loc]:
        #                 break
        #         left_dist = idx - hashMap[color][loc-1]
        #         right_dist = hashMap[color][loc]-idx
        #         ans.append(min(left_dist, right_dist))
        # return ans

        # sol3 3970ms 11.9%
        # O(qlogn+n) O(n)
        # hashMap = {}; ans = []
        # for idx, color in enumerate(colors):
        #     if color in hashMap:
        #         hashMap[color].append(idx)
        #     else:
        #         hashMap[color] = [idx]
        # for [idx, color] in queries:
        #     if color not in hashMap:
        #         ans.append(-1); continue
        #     import bisect
        #     loc = bisect.bisect(hashMap[color], idx)
        #     if loc == 0:
        #         ans.append(hashMap[color][0]-idx)
        #     elif loc == len(hashMap[color]):
        #         ans.append(idx-hashMap[color][-1])
        #     else:
        #         ans.append(min(idx-hashMap[color][loc-1], hashMap[color][loc]-idx))
        # return ans
        pass

    def solve(self, idx, colors, color):
        for i in range(idx, len(colors)):
            if colors[i] == color:
                self.temp = min(i-idx, self.temp); break ;

        for i in range(idx-1, -1, -1):
            if colors[i] == color:
                self.temp = min(idx-i, self.temp); break ;

        pass

print(Solution().shortestDistanceColor([1,1,2,1,3,2,2,3,3],[[1,3],[2,2],[6,1]]))