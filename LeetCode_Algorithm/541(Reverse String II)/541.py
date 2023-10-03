class Solution:
    def reverseStr(self, s: str, k: int) -> str: 
        # sol1 29ms 97% 14MB 59%       
        s = list(s)
        for i in range(0, len(s), 2*k):
            s[i:i+k] = reversed(s[i:i+k])
        return "".join(s)