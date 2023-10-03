'''
leet : 72


word1에서 word2가 되기 위한 단계 수를 구하라
1. 글자 삽입
2. 글자 삭제
3. 글자 교체

# sol1
당연히 단순 대입을 하면 시간 초과가 일어난다.
117ms 68% 19.9MB 60%
mn의 배열을 만든 뒤 각각 글자를 모두 비교해서 달라질 경우를 계산한다.
글자수가 만약 같다면 이전과 동일하게 진행하고 다르면 나온 경우의 수에서 가장 작은 경우의 수를 저장한다.

'''

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word1) + 1) for _ in range(len(word2) + 1)]
        for c in range(len(word1)+1):
            dp[0][c] = c
        for r in range(len(word2) + 1):
            dp[r][0] = r
            
        for r in range(1, len(word2) + 1):
            for c in range(1, len(word1) + 1):
                if word1[c-1] == word2[r-1]:
                    dp[r][c] = dp[r-1][c-1]
                else:
                    dp[r][c] = 1 + min(dp[r-1][c-1], dp[r-1][c], dp[r][c-1])
        return dp[-1][-1]

print(Solution().minDistance("horse", "ros"))
        
