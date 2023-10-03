'''
LeetCode 1466 : Reorder Routes to Make All Paths Lead to the City Zero
directed 그래프에서 0을 제외한 모든 도시에서 0으로 향할 수 있도록 도로를 재구성하려 한다.
방향이 있으므로 역으로 되어있는 길은 방향을 바꿔도 된다.
최소한으로 바꿔도 되는 길의 수를 구하라.

# sol1 1281ms 60% 70.4MB 52%
0에서 부터 시작하여 도시들을 방문한다.
만약 진행하는 길이 원래 있었던 길이라면 답에 1을 더한다.
그리고 깊이를 진행하면서 원래 있었던 길을 따라 가는 값을 리턴한다.

'''
class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        # sol1
        from collections import defaultdict
        self.path = defaultdict(list)
        self.roads = set()
        for [x, y] in connections:
            self.path[x].append(y)
            self.path[y].append(x)
            self.roads.add((x,y))
        self.seen = set([0])
        return self.solve(0)


    def solve(self, city):
        ans = 0
        for p in self.path[city]:
            if p not in self.seen:
                self.seen.add(p)
                if (city, p) in self.roads:
                    ans += 1
                ans += self.solve(p)
        return ans

        

    