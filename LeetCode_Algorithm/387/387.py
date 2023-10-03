from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:

        # sol1 110~140ms 90~65% 보다 빠름
        # hashMap = {}

        # for idx in range(len(s)):
        #     if s[idx] not in hashMap:
        #         hashMap[s[idx]] = idx
        #     else:
        #         hashMap[s[idx]] = -1

        # for chr in hashMap:
        #     if hashMap[chr] >= 0:
        #         return hashMap[chr] 
        #     else: 
        #         continue

        # return -1

        # sol2 n^2 1040ms 8%보다 빠름

        # for i in range(len(s)):
        #     flag = 0
        #     for j in range(len(s)):
        #         if i==j:
        #             continue
        #         if s[i] == s[j]: 
        #             flag = 1
        #             break;
        #     if flag == 0:
        #         return i
        # return -1

        # sol3 150ms 56%보다 빠름
        # 파이썬 특징 collections의 Counter 클래스
        # 문자열의 알파벳을 세어서 딕셔너리로 리턴한다.

        counter = Counter(s)
        for idx, chr in enumerate(s):
            if counter[chr] == 1:
                return idx
        return -1


print(Solution().firstUniqChar("loveleetcode"))