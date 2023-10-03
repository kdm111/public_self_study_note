'''

LeetCode 787 : Cheapest Flights Within K Stops
그래프가 주어질 때 주어진 카운트 내에서 종점에 도달하는 최소 비용을 구하라

# sol1 time limit exceeded
dfs 

# sol2 time limit exceeded
bfs

# sol3 97ms 98% 15.4MB 37%
dijstra
일단 그래프를 만든 뒤 
그래프에서 나아가는 최소 거리를 구하기 위해 cntArr를 만든뒤
민힙에 저장하여 앞자리를 cost로 지정한다. 그렇게 될 경우 민힙이므로 자동으로 가장 작은 값이 찾아 반환되고
가장 적은 거리로 도달하는 경우를 찾는다.

'''
class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        self.graph = {}
        for flight in flights:
            [start, end, cost] = flight
            if start not in self.graph:
                self.graph[start] = [(end, cost)]
            else:
                self.graph[start].append((end, cost))
        # sol1
        # import sys
        # self.ans = sys.maxsize; visited = []
        # self.solve(src, dst, 0, k, 0, visited)

        # sol2
        # import sys
        # ans = sys.maxsize;
        # queue = [[src, 0]]
        # cnt = 0
        # while cnt <= k+1 and queue:
        #     temp = []
        #     while queue:
        #         [station, cost]= queue.pop(0)
        #         if cost > ans:
        #             continue
        #         if station == dst:
        #             ans = min(ans, cost)
        #             continue
        #         if station in self.graph:
        #             for [end, c] in self.graph[station]:
        #                 temp.append([end, cost+c])
        #     queue = temp[:]
        #     cnt += 1
        # return ans if sys.maxsize != ans else -1

        # sol3
        self.graph = {}
        for flight in flights:
            [start, end, cost] = flight
            if start not in self.graph:
                self.graph[start] = [(end, cost)]
            else:
                self.graph[start].append((end, cost))
        import heapq, sys
        stops = [sys.maxsize] * (n + 1)
        queue = [(0, src, -1)]
        while queue:
            cost, curr, cnt = heapq.heappop(queue)
            if curr == dst:
                return cost
            if cnt >= k or cnt >= stops[curr]:
                continue
            stops[curr] = cnt
            if curr in self.graph:
                for v, e in self.graph[curr]:
                    heapq.heappush(queue, (cost+e, v, cnt+1))  
        return -1
                    
            
        
        

    def solve(self, src, dst, cnt, k, temp, visited):
        if k + 1 < cnt or temp > self.ans or src in visited:
            return ;
        visited.append(src)
        if src == dst:
            self.ans = min(self.ans, temp)
            return ;
        if src in self.graph:
            for c in self.graph[src]:
                station, cost = c
                self.solve(station, dst, cnt+1, k, temp + cost)
        



print(Solution().findCheapestPrice(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1))
print(Solution().findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1))

            