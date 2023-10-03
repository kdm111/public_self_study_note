class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:

        # sol1 two pointer 42~50ms 54~31%
        word_idx = 0
        abbr_idx = 0
        while abbr_idx < len(abbr):
            if '1' <= abbr[abbr_idx] <= '9':
                num = ""
                while abbr_idx < len(abbr) and ('0' <= abbr[abbr_idx] <= '9'):
                    num += abbr[abbr_idx]
                    abbr_idx += 1
                word_idx += int(num)
                continue
            if word_idx >= len(word) or (word[word_idx] != abbr[abbr_idx]):
                return False
            else:
                word_idx += 1
                abbr_idx += 1
        return (len(word) == word_idx)





print(Solution().validWordAbbreviation("internationalization", "in4a11o1"))
print(Solution().validWordAbbreviation("a", "2"))
print(Solution().validWordAbbreviation("situation", "9"))
print(Solution().validWordAbbreviation("applae", "appl1e"))
