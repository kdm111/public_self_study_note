class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hashMap = {}
        for i in range(len(order)):
            if order[i] not in hashMap:
                hashMap[order[i]] = i

        for i in range(len(words)-1):
            if (self.check(words[i], words[i+1], hashMap) == False):
                return False
        return True

    def check(self, word1, word2, hashMap):
        i = 0
        while word1[i] and word2[i] and word1[i] == word2[i]:
            i += 1

        if not word1[i]:
            return True
        return False
                