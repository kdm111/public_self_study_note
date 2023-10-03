class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # sol1 53ms 69%        
        s_t = {}
        t_s = {}
        for s_char, t_char in zip(s,t):
            if s_char in s_t:
                if s_t[s_char] != t_char:
                    return False
            else:
                s_t[s_char] = t_char
            if t_char in t_s:
                if t_s[t_char] != s_char:
                    return False
            else:
                t_s[t_char] = s_char
        
        return True

                

        pass

print(Solution().isIsomorphic("badc", "baba"))
print(Solution().isIsomorphic("foo", "baa"))
