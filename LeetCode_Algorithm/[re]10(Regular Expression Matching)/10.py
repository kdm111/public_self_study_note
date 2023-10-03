# unittest
# 파이썬은 유닛테스트를 위한 패키지를 제공하고 있다.
import unittest

class TestSolution(unittest.TestCase):
    def test_0(self):
        s = ""
        p = "a*"
        self.assertTrue(Solution().isMatch(s,p))

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # sol1 154ms 27%
        # dp
        # dp 2d array를 만들어서 각 항까지 True여부를 판단
        # dp[i][j]는 p[:i] == s[:j]라는 뜻
        # dp[0][0]는 s,p가 모두 ""이라는 뜻
        # dp[1][1]은 s[0] == p[0]라는 뜻
        dp = [[False] * (len(s)+1) for _ in range(len(p)+1)]
        # 어떤 상황에서도 dp[0][0]는 True
        dp[0][0] = True
        # s가 빈 스트링이지만 p는 그렇지 않을 때 예외 케이스 처리
        # *가 이전에 존재했던 모든 문자들을 지울 수 있기 때문에
        # dp의 세로줄을 하나 이전의 값으로 업데이트한다. test_0
        for i in range(2, len(p)+1):
            dp[i][0] = dp[i-2][0] and p[i-1] == '*'


        for i in range(1, len(p)+1):
            for j in range(1, len(s)+1):
                if p[i-1] != '*':
                    # 이전 값이 *아니면
                    # dp는 현재까지의 모든 값과  p[i-1] == s[j-1]이거나 p[i-1] == .일경우 참
                    dp[i][j] = dp[i-1][j-1] and (p[i-1] == s[j-1] or p[i-1] == '.')
                else:
                    # 이전에 *가 존재할경우
                    # 하나 이전의 값을 받거나 그 이전의 값을 사용한다.
                    # 
                    dp[i][j] = dp[i-2][j] or dp[i-1][j]
                    # p의 이전 항목이 현재 s와 같을 경우
                    if p[i-2] == s[j-1] or p[i-2] == '.':
                        dp[i][j] = dp[i][j] or dp[i][j-1]
        return dp[-1][-1]

        for i in range(len(dp)):
            print(dp[i], end="\n")

        return True
        pass


if __name__ == "__main__":
    unittest.main()