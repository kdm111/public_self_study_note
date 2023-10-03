'''
LeetCode 841 : Keys and Rooms

0~n-1의 n개의 방이 존재한다. 0번을 제외하고 모든 방은 잠겨있다. 
목표는 모든 방을 방문하는 것이고 열쇠가 없으면 들어갈 수 없다.
모든 방을 방문할 수 있다면 true를 반환하라.

# sol1 65ms 84% 14.9MB 28%
seen에 넣어놓고 0번에서 부터 DFS
'''
class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        seen = set([0])   
        def solve(room_number):
            for canVisit in rooms[room_number]:
                if canVisit not in seen:
                    seen.add(canVisit)
                    solve(canVisit)
        solve(0)
        return len(seen) == len(rooms)