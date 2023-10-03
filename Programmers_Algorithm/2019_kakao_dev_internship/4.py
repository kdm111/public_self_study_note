# 재귀에서 한계 증가
# import sys
# sys.setrecursionlimit(10000000)

def solution(k, room_number):
    hotel = {}
    def solve(room):
        if room not in hotel:
            hotel[room] = room + 1
            return room
        hotel[room] = solve(hotel[room])
        return hotel[room]
    ans = []
    for room in room_number:
        if room not in hotel:
            ans.append(room)
            hotel[room] = room + 1
        else:
            ans.append(solve(room))
    return ans
    

print(solution(10, [1,3,4,1,3,4]))
# print(solution(1, [2]))
# print(solution(2, [2]))

