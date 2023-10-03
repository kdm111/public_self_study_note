class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # sol1 O(m), O(1) 44~50ms 57~41%
        # m is length of target string
        sIdx = 0; tIdx = 0
        while sIdx < len(s) and tIdx < len(t):
            if s[sIdx] == t[tIdx]: 
                sIdx += 1; tIdx += 1
            elif s[sIdx] != t[tIdx]:
                tIdx += 1
        return sIdx == len(s)


print(Solution().isSubsequence("abc", "ahbgdc"))