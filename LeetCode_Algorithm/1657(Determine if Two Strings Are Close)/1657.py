'''

271ms 41% 17.8MB 20%
'''
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if set(word1) != set(word2):
            return False
        word1_cnt = self.makeCnt(self.makeMap(word1))
        word2_cnt = self.makeCnt(self.makeMap(word2))
        word1_cnt.sort(); word2_cnt.sort()
        for i in range(len(word1_cnt)):
            if word1_cnt[i] != word2_cnt[i]:
                return False
        return True

    def makeCnt(self, hashMap):
        ret = []
        for c in hashMap:
            ret.append(hashMap[c])
        return ret

    def makeMap(self, word):
        hashMap = {}
        for c in word:
            if c not in hashMap:
                hashMap[c] = 1
            else:
                hashMap[c] += 1
        return hashMap


    
    def makeCnt(self, hashMap):
        ret = []
        for c in hashMap:
            ret.append(hashMap[c])
        return ret

    def makeMap(self, word):
        hashMap = {}
        for c in word:
            if c not in hashMap:
                hashMap[c] = 1
            else:
                hashMap[c] += 1
        return hashMap
print(Solution().closeStrings("abc", "cab"))
        