'''
LeetCode 1576 : Replace All ?'s to Avoid Consecutive Repeating Characters
문자열에서 ?문자를 대체하되 연속된 글자가 오지 못하게 하라

# sol1 39ms 86% 13.9MB 75%
O(n) O(1)
하나하나 비교해서 바꾸기
'''
class Solution:
    def modifyString(self, s: str) -> str:
        # sol1
        s = list(s)
        for i in range(len(s)):
            if s[i] == '?':
                for c in "abc":
                    if i-1 >= 0 and s[i-1] == c: continue
                    if i+1 < len(s) and s[i+1] == c: continue
                    s[i] = c
        return "".join(s)
                    


            
                

print(Solution().modifyString("?ab"))