'''
LeetCode 389 : Find the Difference
두 문자열에서 다른 부분 한 가지를 찾아 리턴하라

# sol1 34ms 91% 13.9MB 74%
# O(n) O(1)
해쉬맵에 저장한뒤 차이나는 글자를 체크

'''
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sLetters = {}
        for c in range(ord('a'), ord('z')+1):
            sLetters[chr(c)] = 0
        for c in s:
            sLetters[c] += 1
        for c in t:
            sLetters[c] -= 1
            if sLetters[c] < 0:
                return c