from typing import List
'''
LeetCode 947 : Most Stones Removed with Same Row or Column
2d 좌표가 존재할 때 n개의 스톤이 좌표를 가지고존재한다.
스톤은 서로 같은 x축이나 같은 y축을 가진다면 하나는 삭제될 수 있다.
지울 수 있는 최대의 스톤을 구하라.

sol1 T : 857ms 35% S : 15.1MB 36%
그래프를 만든 뒤 dfs를 사용해서 계속해서 탐색한다.
루프를 제거하기 위해 rest_stones를 만들어 삭제한다.
'''
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:

        # sol1 dfs
        from collections import defaultdict
        self.r_graph = defaultdict(list); self.c_graph = defaultdict(list)
        for [r,c] in stones:
            self.r_graph[r].append(c)
            self.c_graph[c].append(r)
        
        cnt = 0; self.rest_stones = [(r,c) for [r,c] in stones]
        for [r,c] in stones:
            if (r,c) in self.rest_stones:
                self.dfs(r,c)
                cnt += 1
        return len(stones)-cnt
    def dfs(self, r,c):
        self.rest_stones.remove((r,c))
        for i in self.r_graph[r]:
            if (r,i) in self.rest_stones:
                self.dfs(r,i)
        for j in self.c_graph[c]:
            if (j,c) in self.rest_stones:
                self.dfs(j,c)
            
            
            
            

            
        

print(Solution().removeStones([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]))
        

        
