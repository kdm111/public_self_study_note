from pydoc import ispackage


class Solution:
    def longestPalindrome(self, s: str) -> str:

        #sol1 time exceeded
        # ans = ""
        # for start in range(len(s)):
        #     for end in range(len(s)-1, start-1, -1):
        #         temp = s[start:end+1]
        #         if temp == temp[::-1] and len(temp) > len(ans):
        #             ans = temp
        #             break
        #     start += len(ans)
        # return ans

        # sol2 O(n^2) 1449ms 46%
        ans = ""
        for start in range(len(s)):
            temp1 = self.isPalindrome(s, start, start) # odd
            temp2 = self.isPalindrome(s, start, start+1) # even
            ans = temp1 if len(ans) < len(temp1) else ans
            ans = temp2 if len(ans) < len(temp2) else ans
        return ans

    def isPalindrome(self, s, start, end):
        while 0 <= start and end < len(s) and s[start] == s[end]:
            start -= 1
            end += 1
        return s[start+1:end]





# print(Solution().longestPalindrome("bbbb"))
print(Solution().longestPalindrome("bbbbb"))
# print(Solution().longestPalindrome("ba"))

