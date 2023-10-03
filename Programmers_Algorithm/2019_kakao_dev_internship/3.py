def solution(all_users, all_banned):
    # dfs + board
    ans = set([])
    board = [[0] * len(all_users) for _ in range(len(all_banned))]
    for r in range(len(board)):
        for c in range(len(board[0])):
            if match(all_users[c], all_banned[r]):
                board[r][c] = 1
    visited = []
    def solve(r):
        if r == len(board):
            ans.add("".join(sorted(visited)))
            return 1;
        for c in range(len(board[r])):
            if board[r][c] == 1 and str(c) not in visited:
                visited.append(str(c))
                solve(r+1)
                visited.pop()
    solve(0)
    return len(ans)

# def check(comb, all_banned, temp, ans):
#     if all(condition == '' for condition in all_banned):
#         temp = "".join(sorted(temp))
#         if temp not in ans:
#             ans.add(temp)
#         return
#     for i in range(len(comb)):
#         for j in range(len(all_banned)):
#             if match(comb[i], all_banned[j]):
#                 user_temp = comb[i]; ban_temp = all_banned[j]
#                 comb[i] = ""; all_banned[j] = ""
#                 temp.append(str(i))
#                 check(comb, all_banned, temp, ans)
#                 temp.pop()
#                 comb[i] = user_temp; all_banned[j] = ban_temp

# def makeAllComb(allComb, user_id, idx, totalLen, temp):
#     if len(temp) == totalLen:
#         allComb.append(temp[:])
#         return ;
#     for i in range(idx, len(user_id)):
#         temp.append(user_id[i])
#         makeAllComb(allComb, user_id, i+1, totalLen, temp)
#         temp.pop()

def match(user, banned):
    if not user or not banned:
        return False
    if len(user) != len(banned):
        return False
    i = 0
    while i < len(user):
        if banned[i] != '*' and banned[i] != user[i]:
            return False
        i += 1
    return True
    
    
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))
