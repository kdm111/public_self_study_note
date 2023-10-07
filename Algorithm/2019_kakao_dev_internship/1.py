def solution(board, moves):
    ans = 0
    stack = []
    for m in moves:
        m -= 1
        for r in range(len(board)):
            if board[r][m] != 0:
                stack.append(board[r][m])
                board[r][m] = 0
                break
        if len(stack) >= 2 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
            ans += 2
    return ans

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))