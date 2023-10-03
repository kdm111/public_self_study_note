from typing  import List
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # # sol1 time exceeded
        # station_bus = {}
        # for bus, route in enumerate(routes):
        #     for station in route:
        #         if station not in station_bus:
        #             station_bus[station] = [bus]
        #         else:
        #             station_bus[station].append(bus)
        # visited = []
        # from collections import deque
        # import sys
        # ans = sys.maxsize
        # queue = deque([(source, 0)])

        # # bfs 돌리는 부분에서 시간초과 발생
        # while queue:
        #     cur_station, k = queue.popleft()
        #     if cur_station == target:
        #         return k
        #     visited.append(cur_station)
        #     for bus in station_bus[cur_station]: 
        #         for station in routes[bus]:
        #             if station in visited:
        #                 continue
        #             queue.append((station, k+1))
        # return -1

        # sol2 bfs 819~1291ms 45~19%
        # bus를 visited check 해야 함
        if source == target: return 0

        station_bus = {}
        for bus, route in enumerate(routes):
            for station in route:
                if station not in station_bus:
                    station_bus[station] = [bus]
                else:
                    station_bus[station].append(bus)

        from collections import deque
        queue = deque([(source, 0)])
        bus_visited = [];
        while queue:
            station, k = queue.popleft()
            if station == target:
                return k
            for bus in station_bus[station]:
                if bus not in bus_visited:
                    for station in routes[bus]:
                        queue.append((station, k+1))
                    bus_visited.append(bus)
        return -1

        

print(Solution().numBusesToDestination([[1,2,7],[3,6,7]],1, 6))
print(Solution().numBusesToDestination([[7,12],[4,5,15],[6],[15,19],[9,12,13]],15, 12))

