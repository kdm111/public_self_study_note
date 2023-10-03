class Solution:
    def countSegments(self, s: str) -> int:
        # sol1 T : 46ms 67% S : 13.9MB 6%
        # i = 0; cnt = 0;
        # while i < len(s):
        #     while i < len(s) and s[i] == ' ':
        #         i += 1
        #     if i < len(s):
        #         cnt += 1
        #     while i < len(s) and s[i] != ' ':
        #         i += 1
        # return cnt

        # sol2 T : 62ms 17% S : 13.9MB 48%
        return len(s.split())



print(Solution().countSegments("aa bb"))