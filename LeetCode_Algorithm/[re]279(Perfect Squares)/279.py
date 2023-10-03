'''
LeetCode 279 : Perfect Squares
정사각형의 면적을 차례로 제거해 가면서 
면적 n에 들어가는 최소의 정사각형 개수 구하기
n은 1~10**4이다.

# sol1 time limit exceeded n = 7168
n에 들어갈 수 있는 모든 정사각형의 면적을 구한 뒤
dfs를 활용해서 최소 정사각형 개수를 구함

# sol2 5945ms 17% 14.1MB 59%

'''
class Solution:
    def numSquares(self, n: int) -> int:
    #     from math import sqrt
    #     import sys
    #     # sol1
    #     self.squares = []
    #     for i in range(1, int(sqrt(n)+1)):
    #         self.squares.append(i * i)
    #     self.ans = sys.maxsize
    #     self.dfs(n, 0)
    #     return self.ans
    # def dfs(self, n, k):
    #     if k >= self.ans:
    #         return ;
    #     if n == 0:
    #         self.ans = min(self.ans, k)
    #     for i in range(len(self.squares)-1, -1, -1):
    #         if n % self.squares[i] == 0:
    #             n -= self.squares[i]
    #             self.dfs(n, k+1)
    #             n += self.squares[i]
        # sol2 
        import sys
        dp = [0] + [sys.maxsize] * n
        for i in range(1, n+1):
            dp[i] = min(dp[i-j*j] for j in range(1, int(i**0.5)+1)) + 1
        return dp[n]
        

        
print(Solution().numSquares(13))