'''
LeetCode 91 : Decode Ways
숫자로 이루어진 문자열이 들어올 때 각 숫자를 문자로 변환하는 방법을 제시하라
"11" -> "AA" "K"

# sol1 37ms 81% 13.8MB 80%
O(n) O(n)
dp로 이전까지 있던 가지 수를 len(s)로 dp를 도출한다.
'0'이라면 디코딩을 할 수 없으므로 0을 리턴한다.
이전에 있는 글자가 0이 아니라면 이어져서 간다.
이전에 있던 두 글자가 10에서 26이하라면 현재에 더한다.

'''
class Solution:
    def numDecodings(self, s: str) -> int:
        # sol1
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        if s[0] != '0': dp[1] = 1
        for i in range(2, len(dp)):
            if s[i - 1] != '0':
                dp[i] = dp[i - 1]
            if 10 <= int(s[i - 2 : i]) <= 26:
                dp[i] += dp[i - 2]
        return dp[len(s)]
            
            
print(Solution().numDecodings("226")) 
print(Solution().numDecodings("204")) 
print(Solution().numDecodings("11106"))
print(Solution().numDecodings("11"))



'''
226
2 2 6
22 6
2 26
26 2

2 2 6
1 2 4

2 0 4
1 1 1

266
2 6 6 
26 6

2 6 6
1 2 2

11106
1 1 10 6
11 10 6

1 1 1
11 1

11106
12

111
12

1 1 1
11 1
1  11
'''