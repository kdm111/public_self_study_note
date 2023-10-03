from typing import List

'''
LeetCode 1662 
두 문자열 리스트가 같은 문자열을 가리키는 지 확인
 sol1 T : 48ms 74% S : 13.9MB 33%
 T : O(n) S : O(1)
 두 문자열을 비교하면서 상황에 맞을 때마다 시스트 인덱스와 문자열 인덱스를 업데이트

 sol2 T : 39ms 85% S : 13.9MB 33%
 T : O(n) S : O(n)
 파이썬 내장 함수를 사용해 두 리스트를 문자열로 만들어 비교
'''
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        # sol1
        idx1 = 0; idx2 = 0
        str1_idx = 0; str2_idx = 0
        while idx1 < len(word1) or idx2 < len(word2):
            if idx1 == len(word1) or idx2 == len(word2):
                return False
            if word1[idx1][str1_idx] != word2[idx2][str2_idx]:
                return False
            str1_idx, str2_idx = str1_idx + 1, str2_idx + 1
            if str1_idx == len(word1[idx1]):
                idx1, str1_idx = idx1 + 1, 0
            if str2_idx == len(word2[idx2]):
                idx2, str2_idx = idx2 + 1, 0
        return True

        # sol2
        return "".join(word1) == "".join(word2)

print(Solution().arrayStringsAreEqual(["a", "b"], ["a", "b"]))