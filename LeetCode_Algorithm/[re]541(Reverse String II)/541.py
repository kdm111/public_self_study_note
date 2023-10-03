class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        r = list(reversed(s[:k])); p = s[k:]   
        return "".join(r + p)



print(Solution().reverseStr("abcd", 2))
print(Solution().reverseStr("adffff", 3))
