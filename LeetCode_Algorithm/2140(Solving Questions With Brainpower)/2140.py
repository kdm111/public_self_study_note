'''
LeetCode 2140 : Solving Questions With Brainpower
문제가 [점수, 난이도]로 주어진다.
난이도는 문제를 해결한 후 그 뒤에 난이도 만큼 문제를 해결하지 못한다.

# sol1
'''
class Solution:
    def mostPoints(self, questions: list[list[int]]) -> int:
        # sol1
        # def dp(i):
        #     if i >= len(questions):
        #         return 0
        #     j = i + questions[i][1] + 1
        #     return max(questions[i][0] + dp(j), dp(i + 1))
        # return dp(0)

        # sol2 1626ms 72% 60MB 98%
        dp = [0] * (len(questions) + 1)
        for i in range(len(questions)-1, -1, -1):
            j = i + questions[i][1] + 1
            dp[i] = max(questions[i][0] + dp[min(j, len(questions))], dp[i + 1])
        return dp[0]



    

