from collections import deque
def solution(rc, operations):
    M = len(rc); N = len(rc[0])
    left = deque([rc[i][0] for i in range(M)])
    right = deque([rc[i][-1] for i in range(M)])
    rows = deque(deque(rc[i][1:N-1]) for i in range(M))
    
    for op in operations:
        if op == "ShiftRow":
            left.appendleft(left.pop())
            rows.appendleft(rows.pop())
            right.appendleft(right.pop())
        else:
            rows[0].appendleft(left.popleft())
            right.appendleft(rows[0].pop())
            rows[M-1].append(right.pop())
            left.append(rows[M-1].popleft())
    ans = []
    for _ in range(M):
        ans.append([left.popleft()] + list(rows.popleft()) + [right.popleft()])
    return ans
def rotate(rc):
    ret = [[None] * len(rc[0]) for _ in range(len(rc))]
    for i in range(len(ret[0])-1):
        ret[0][i+1] = rc[0][i]
    for r in range(len(ret)-1):
        ret[r+1][-1] = rc[r][-1] 
    for c in range(len(ret[0])-1, 0, -1):
        ret[len(ret)-1][c-1] = rc[len(rc)-1][c]
    for r in range(len(ret)-1, 0, -1):
        ret[r-1][0] = rc[r][0]
    for r in range(len(rc)):
        for c in range(len(rc[0])):
            if ret[r][c] == None:
                ret[r][c] = rc[r][c]
    return ret
        
print(solution([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], ["Rotate", "ShiftRow"]))