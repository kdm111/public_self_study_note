class Solution:
    def reverseWords(self, s: str) -> str:
        # sol1 41ms 85% 14MB 79%
        ans = "";
        left, right = len(s)-1, len(s)-1
        start = 0
        while s[start] == ' ':
            start += 1
        while s[left] == ' ':
            left -= 1
        while left >= start:
            right = left
            while s[left] != ' ' and left >= start:
                left -= 1
            temp = s[left+1 : right+1]
            ans += temp
            while s[left] == ' ' and left >= start:
                left -= 1
            if left >= start:
                ans += ' '
        return ans

        # sol2 84ms 16% 13.9MB 80%
        return " ".join(reversed(s.split()))
        # sol3
        
print(Solution().reverseWords("a sky       is blue    "))