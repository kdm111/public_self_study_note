class Solution:
    def wordSubsets(self, words1: list[str], words2: list[str]) -> list[str]:
        ans = []
        hashMap = {}
        for word in words2:
            for c in word:
                if c not in hashMap:
                    hashMap[c] = 1
                else:
                    hashMap[c] += 1
        for word in words1:
            word_hashMap = {}
            for c in word:
                if c not in word_hashMap:
                    word_hashMap[c] = 1
                else:
                    word_hashMap[c] += 1
            flag = True
            for k in hashMap:
                if k not in word_hashMap or word_hashMap[k] < hashMap[k]:
                    flag = False; break
            if flag:
                ans.append(word)
        return ans
        

print(Solution().wordSubsets(["amazon","apple","facebook","google","leetcode"], ["e","o"]))