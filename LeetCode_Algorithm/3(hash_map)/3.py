import string


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sol1 O(2n) O(n) 65ms 85%
        string = ""
        ans = 0
        for char in s:
            string = self.solve(string, char)
            if ans < len(string):
                ans = len(string)
        return ans
    def solve(self, string: str, char: chr):
        for idx in range(len(string)):
            if string[idx] == char:
                string = string[idx+1:]
                break ;
        string += char
        return string
        

print(Solution().lengthOfLongestSubstring("dvdf"))