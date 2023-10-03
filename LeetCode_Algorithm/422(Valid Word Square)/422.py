from typing import List
class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        # sol1 T : 167ms 41% S : 14.7MB 46%
        # O(n) O(n)
        for i in range(len(words)):
            if self.check(words, i) == False:
                return False
        return True
    def check(self, words, i):
        str1 = words[i]
        str2 = ""
        j = 0
        try:
            while j < len(words[i]):
                str2 += words[j][i]
                j += 1
            return str1 == str2
        except:
            return False
print(Solution().validWordSquare(["abcd","bnrt","crmy","dt"]))