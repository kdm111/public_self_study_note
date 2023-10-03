'''
LeetCode 44 : Wildcard Matching

'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i = j = 0
        while i < len(s) and j < len(p):
            if p[j] == '?':
                i += 1
            elif p[j] == '*':
                while j < len(p) and i < len(s) and s[i+1] == p[j+1]:
                    i += 1; j += 1
            elif p[j] == s[i]:
                i += 1
            else:
                return False
            j += 1
        return True if i == len(s) else False