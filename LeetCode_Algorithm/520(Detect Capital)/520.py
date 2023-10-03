class Solution:
    # 23ms 99% 13.9MB 56%
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True
        if not self.isCapital(word[0]) and self.isCapital(word[1]):
            return False
        capital = self.isCapital(word[1])
        for i in range(2, len(word)):
            if capital != self.isCapital(word[i]):
                return False
        return True
    def isCapital(self, c):
        return c >= 'A' and c <= 'Z'
print(Solution().detectCapitalUse("Leet"))