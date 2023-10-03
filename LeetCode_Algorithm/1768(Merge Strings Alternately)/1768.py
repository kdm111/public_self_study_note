'''
LeetCode 1768

문자열로 합성을 하거나 다루는 기능을 지원하는 언어는 몇가지 존재하지 않는다.
그래서 배열을 활용하여 한꺼번에 문자열로 변환하는 것이 더 빠르다.

'''
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # sol1 39ms 12% 13.8MB 55%
        # ans = ""
        # i = 0; j = 0
        # while i < len(word1) or j < len(word2):
        #     if i < len(word1):
        #         ans += word1[i]; i += 1
        #     if j < len(word2):
        #         ans += word2[j]; j += 1
        # return ans

        # sol2 30ms 73% 13.8MB 96%
        # if word1[0] and word2[0]:
        #     return word1[0] + word2[0] + \
        #         self.mergeAlternately(word1[1:], word2[1:])
        # return word1 if word1 else word2

        # sol3 32ms 58% 14MB 9%
        ans = []; i = 0;
        word1Len = len(word1); word2Len = len(word2)
        while i < word1Len or i < word2Len:
            if i < word1Len:
                ans.append(word1[i])
            if i < word2Len:
                ans.append(word2[i])
            i += 1
        return "".join(ans)
        
print(Solution().mergeAlternately("abc", "defd"))