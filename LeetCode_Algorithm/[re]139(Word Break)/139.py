'''
LeetCode 139 : Word Break
주어진 문자열이 wordDict안의 있는 글자들로 구분될 수 있는지 구하라

# sol1
dp로 문자수를 체크한다.
이제 문자들을 하나하나 슬라이싱 한 뒤 
2중 반복문을 통해 모든 가질 수 있는 모든 문자열을 구한다.
시작점이 가능하고 가질 수 있는 문자열이 wordDict에 존재할 경우 그 끝을 참으로 만든다.


'''
class Solution:

    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        # sol1
        dp = [False] * (len(s)+1)
        dp[0] = True
        for i in range(len(s)):
            for e in range(i+1, len(s)+1):
                if dp[i] and s[i:e] in wordDict:
                    dp[e] = True
        return dp[-1]
                    
            
        
        
        
print(Solution().wordBreak("leetcode", ["leet", "code"]))