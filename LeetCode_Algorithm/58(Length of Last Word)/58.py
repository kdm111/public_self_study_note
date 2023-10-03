class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # sol1 38ms 62%
        # ans = 0
        # check = 0
        # for char in s[::-1]:
        #     if check and char == ' ':
        #         break
        #     if char == ' ':
        #         pass
        #     if ('a' <= char <= 'z') or ('A' <= char <='Z'):
        #         check = 1
        #         ans += 1
        # return ans

        # sol2 39ms 58%
        s = s.rstrip()
        ans = 0
        for char in s[::-1]:
            if char == ' ': break
            ans += 1
        return ans

print(Solution().lengthOfLastWord("adf ahpe   "))