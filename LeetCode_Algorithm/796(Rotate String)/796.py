class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # sol1 57ms 41%
        # 하나씩 다 넘겨가면서 테스트
        i = 0
        while (i < len(s)):
            if self.stringEqual(s, goal):
                return True
            s = s[1:] + s[0]
            i += 1
        return False
    def stringEqual(self, s, g):
        i = 0
        while i < len(s) and i < len(g):
            if s[i] == g[i]:
                i += 1
            else:
                break
        return True if i  == len(s) else False
