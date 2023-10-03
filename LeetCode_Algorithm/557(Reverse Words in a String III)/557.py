class Solution:
    def reverseWords(self, s: str) -> str:

        # sol1
        # O(n) O(n)
        # ans = ""; temp = ""
        # for c in s:
        #     if c == ' ':
        #         ans += "".join(reversed(list(temp)))
        #         ans += ' '
        #         temp = ""
        #     else:
        #         temp += c
        # ans += "".join(reversed(list(temp)))
        # return ans

        # sol2 154ms 14%
        # O(n) O(1)
        # s = list(s)
        # left = 0; right = 0
        # while right < len(s):
        #     while right < len(s) and s[right] != ' ':
        #         right += 1
        #     right -= 1
        #     while left < right:
        #         s[left],s[right] = s[right],s[left]
        #         left += 1; right -= 1
        #     while left < len(s) and s[left] != ' ':
        #         left += 1
        #     left += 1; right = left
        
        # return "".join(s)



print(Solution().reverseWords("abc def"))
        