'''
LeetCode 1143 : Longest Common Subsequence

'''
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # sol1 하향식 time limit exceeded
        # def dp(i, j):
        #     if i == len(text1) or j == len(text2):
        #         return 0
        #     if text1[i] == text2[j]:
        #         return 1 + dp(i+1, j+1)
        #     else:
        #         return max(dp(i+1, j), dp(i, j+1))
        # return dp(0, 0)

        # sol2 상향식 825ms 78% 39.1MB 71%
        # dp = [[0] * (len(text2) + 1) for _ in range(len(text1)+1)]
        # for i in range(len(text1)-1, -1, -1):
        #     for j in range(len(text2)-1, -1, -1):
        #         if text1[i] == text2[j]:
        #             dp[i][j] = 1 + dp[i + 1][j + 1]
        #         else:
        #             dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        # return dp[0][0]
    
        # sol3 O(mn) 568ms 85% 41.35MB 84%
        dp = [[0] * (len(text1)+1) for _ in range(len(text2)+1)]
        for i in range(len(text2)):
            for j in range(len(text1)):
                if text1[j] == text2[i]: 
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        return dp[-1][-1]
        
            
print(Solution().longestCommonSubsequence("abcde", "ace"))
print(Solution().longestCommonSubsequence("bsbininm", "jmjkbkjkv"))

            
        
    