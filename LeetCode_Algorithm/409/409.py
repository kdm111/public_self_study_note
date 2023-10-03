class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashMap = {}
        for char in s:
            if char not in hashMap:
                hashMap[char] = 1
            else:
                hashMap[char] += 1

        ans = 0
        for key in hashMap:
            ans += (hashMap[key] // 2) * 2
            if ans % 2 == 0 and hashMap[key] % 2 == 1:
                ans += 1
        return ans


print(Solution().longestPalindrome("abccccdd"))