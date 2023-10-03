'''
일반 dfs는 시간 초과 걸림. 이걸로 1시간 소요
재귀도 시간 초과 걸림. 이걸로 1시간 반 소요
표준 라이브러리를 적극적으로 사용해야 한다.
'''


from collections import defaultdict, deque
def solution(n, paths, gates, summits):
    summits.sort(); gates.sort()
    summits = set(summits); gates = set(gates)
    board = defaultdict(set)

    for path in paths:
        if path[0] in gates or path[1] in summits:
            board[path[0]].add((path[1], path[2]))
        else:
            board[path[0]].add((path[1], path[2]))
            board[path[1]].add((path[0], path[2]))

    intensity = [999999999] * (n + 1)
    a = [999999999, 999999999]
    for gate in gates:
        queue = deque([(gate, -1)])
        while queue:
            (x, y) = queue.popleft()
            for (g, w) in board[x]:
                if intensity[g] > max(w, y): 
                    intensity[g] = max(w, y)
                    if g in summits:
                        if intensity[g] < a[1]:
                            a = [g, intensity[g]]
                        elif intensity[g] == a[1]:
                            a[0] = min(a[0], g)
                    else:
                        queue.append((g, max(w, y)))

    return a
print(solution(7, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], \
               [1,3], [5]))

print(solution(4, [[1, 3, 1], [1, 4, 1], [4, 2, 1]], \
               [1], [2,3,4]))

print(solution(7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], \
               [1], [2,3,4]))