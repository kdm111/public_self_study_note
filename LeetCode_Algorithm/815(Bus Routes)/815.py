from typing import List
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # sol1 1071ms 27%
        if source == target:
            return 0
        bus_stop_hashMap = {}
        for bus in range(len(routes)):
            for stop in routes[bus]:
                if stop not in bus_stop_hashMap:
                    bus_stop_hashMap[stop] = [bus]
                else:
                    bus_stop_hashMap[stop].append(bus)
        # print(routes)
        # print(bus_stop_hashMap)
        # import sys
        # ans = sys.maxsize; queue = [(source, 0)]
        # seen_bus = set(); seen_stop = set([source]);
        # while queue:
        #     curr, temp_ans = queue.pop(0)
        #     if curr == target:
        #         return temp_ans
        #     for bus in bus_stop_hashMap[curr]:
        #         if bus not in seen_bus:
        #             for stop in routes[bus]:
        #                 if stop not in seen_stop:
        #                     queue.append((stop, temp_ans+1))
        #                     seen_stop.add(stop)
        #         seen_bus.add(bus)
        # return -1 if ans == sys.maxsize else ans

print(Solution().numBusesToDestination([[1,2,7],[3,6,7]], 1, 6))
print(Solution().numBusesToDestination([[7,12],[4,5,15],[6],[15,19],[9,12,13]], 15, 12))
