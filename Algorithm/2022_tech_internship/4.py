'''
목표값을 잘 조절한 뒤 그 이상을 계산하지 말 것
조건을 잘 따져서 도달할 해도 되는 부분 까지만 계산할 것.
그 이상 초과하면 미만으로 낮춰서 계산
'''
def solution(alp, cop, problems):
    max_algo = alp; max_code = cop;
    for i in range(len(problems)):
        max_algo = max(max_algo, problems[i][0])
        max_code = max(max_code, problems[i][1])

    dp = [[100000] * (max_code + 1) for _ in range(max_algo+1)]
    dp[alp][cop] = 0
    for a in range(alp, max_algo+1):
        for c in range(cop, max_code+1):
            if a+1 <= max_algo:
                dp[a+1][c] = min(dp[a+1][c], dp[a][c]+1)
            if c+1 <= max_code:
                dp[a][c+1] = min(dp[a][c+1], dp[a][c]+1)
            
            for (alp_req, cop_req, alp_rwd, cop_rwd, cost) in problems:
                if a >= alp_req and c >= cop_req:
                    i = min(a + alp_rwd, max_algo)
                    j = min(c + cop_rwd, max_code)
                    dp[i][j] = min(dp[i][j], dp[a][c]+cost)

    return dp[max_algo][max_code]

print(solution(10, 10, [[10,15,2,1,2],[20,20,3,3,4]]))
print(solution(0, 0, [[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]))
# print(solution(0, 0, [
#         [0, 0, 1, 1, 1],
#         [150, 150, 1, 1, 100],
#     ]))
# print(solution(0, 0, [
#         [4, 3, 1, 1, 100],
#         [0, 0, 2, 2, 1],
#     ]))

# print(solution(1, 1, [
#         [0, 2, 1, 1, 100]
#     ]))
# print(solution(1, 1, [
#         [2, 0, 1, 1, 100],
#     ]))

# print(solution(2, 2, [
#         [1, 1, 1, 1, 100],
#     ]))

# print(solution(10, 10, [
#         [0, 0, 5, 5, 1],
#         [30, 10, 1, 1, 100],
#     ]))

# print(solution(0, 0, [
#         [0, 0, 30, 2, 1],
#         [150, 150, 30, 30, 100],
#     ]))
