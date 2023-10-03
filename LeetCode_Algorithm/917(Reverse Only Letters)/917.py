'''
LeetCode 917 : Reverse Only Letters
주어진 문자열이 있을 때 규칙에 따라 문자를 뒤집어라.
영어가 아닌 경우 문자는 그 위치에 그대로 남아야 한다.
영어는 뒤집어야 한다.

# sol1 32ms 74% 14MB 11%
ans를 초기화 하고 영어가 아닌 문자들을 먼저 배치 한 뒤 
영어를 뒤집어서 넣음

# sol2 22ms 98% 13.9MB 58%
two stack 
두 개의 스택에 저장해 놓고 영어는 거꾸로 넣고 글자는 그냥 넣기
'''


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        # sol1
        # idx = 0
        # ans = [' ' for _ in range(len(s))]
        # while idx < len(s):
        #     if not s[idx].isalpha():
        #         ans[idx] = s[idx]
        #     idx += 1
        # ansIdx = 0; idx = len(s)-1
        # while True:
        #     while ansIdx < len(ans) and ans[ansIdx] != ' ':
        #         ansIdx += 1
        #     while idx >= 0 and not s[idx].isalpha():
        #         idx -= 1
        #     if ansIdx < len(ans) and idx >= 0:
        #         ans[ansIdx] = s[idx]
        #         ansIdx += 1
        #         idx -= 1
        #     else:
        #         break
        # return "".join(ans)

        # sol2
        # eng = []
        # others = []
        # ans = []
        # for c in s:
        #     if c.isalpha():
        #         eng.append(c)
        #     else:
        #         others.append(c)
        # for i in range(len(s)):
        #     if not s[i].isalpha():
        #         c = others.pop(0)
        #         ans.append(c)
        #     else:
        #         c = eng.pop()
        #         ans.append(c)
        # return "".join(ans)

        # sol3 33ms 86% 16.09MB 98%
        # O(n) O(n) 
        ans = ""
        i, j = 0, len(s)-1
        while i < len(s):
            if s[i].isalpha():
                while j > 0 and not s[j].isalpha():
                    j -= 1
                ans += s[j]
                j -= 1
            else:
                ans += s[i]
            i += 1
        return ans
                
    
print(Solution().reverseOnlyLetters("?6C40E"))
print(Solution().reverseOnlyLetters("----"))
print(Solution().reverseOnlyLetters("babaab"))
print(Solution().reverseOnlyLetters("dc-ba"))
print(Solution().reverseOnlyLetters("a-bC-dEf-ghIj"))
print(Solution().reverseOnlyLetters("Test1ng-Leet=code-Q!"))





        
'''
?6E40C
?6E4C0

?6C40E
?6E40
'''