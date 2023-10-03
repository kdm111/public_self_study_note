'''
LeetCode 93 : Restore IP Addresses
숫자로 이루어진 문자열이 주어질 때 가능한 IP를 모두 리턴하라.

# sol1 35ms 86% 14MB 31%
재귀 함수
'''
class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        self.ans = []
        self.solve(s, [])
        return self.ans

    def solve(self, s, temp):
        if len(temp) == 4:
            if len(s) > 0:
                return ;
            string = "".join(temp);
            string = string[0:len(string)-1]
            self.ans.append(string)
            return ;
        i = 1
        while i < 4:
            if i <= len(s):
                if 0 <= int(s[:i]) <= 255:
                    if len(s[:i]) > 1 and s[0] == '0':
                        i += 1
                        continue
                    temp.append(s[:i] + '.')
                    self.solve(s[i:], temp)
                    temp.pop()
            i += 1

print(Solution().restoreIpAddresses("25525511135"))
            

            