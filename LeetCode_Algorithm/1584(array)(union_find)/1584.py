from re import L
from typing import List
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # sol1 kruskal algorithm
        # 점들이 주어진다. 일단 각각 거리를 구해야 한다.
        # self.length라는 함수를 만든 뒤
        hashMap = [list() for _ in range(len(points))]
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                l = self.length(points[i], points[j])
                hashMap[i].append((j, l))
                hashMap[j].append((i, l))
        print(hashMap)

        pass
    def length(self, p1, p2):
        return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
        

print(Solution().minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]))