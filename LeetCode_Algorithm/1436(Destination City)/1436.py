'''
leet : 1436 Destination City
문자열로 들어오는 paths가 존재한다.
start, destination이 존재한다.
최종 도착점을 구하라. 하나의 시작점에는 단 하나의 도착점이 존재한다.


# sol1
# 그래프를 그려서 해결한다.
O(2n) O(n)
66ms 30% 16.3MB 50%

# sol2 60ms 71% 16.3MB 50%
O(n) O(2n)
파이썬은 set의 연산이 가능하다.
set의 연산을 이용하여 결과를 계산한다.
'''
class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        # sol1
        # ans = ""
        # graph = {}
        # for path in paths:
        #     graph[path[0]] = path[1]
        #     if path[1] not in graph:
        #         ans = path[1]
        # while ans in graph:
        #     ans = graph[ans]
        # return ans

        # sol2
        totalStarts = set([])
        totalDests = set([])
        for path in paths:
            totalStarts.add(path[0])
            totalDests.add(path[1])
        return (totalDests - totalStarts).pop()

print(Solution().destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))