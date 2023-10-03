'''
LeetCode 1165 : Single-Row Keyboard
주어진 키 배열이 시작할 때 주어진 word를 타이핑 하려면 이동하는 인덱스는 얼마인가?
주어지는 키는 26개로 고정

# sol1 47ms 91% 13.9MB 84%
# O(n) O(1)
주어진 키 배열을 인덱스와 해쉬맵으로 저장한 뒤 word를 돌면서 타이핑의 거리를 구함
'''

class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        # sol1
        hashMap = {}
        for i in range(len(keyboard)):
            hashMap[keyboard[i]] = i
        ans = curr = 0
        for c in word:
            ans += abs(hashMap[c] - curr)
            curr = hashMap[c]
        return ans

print(Solution().calculateTime("pqrstuvwxyzabcdefghijklmno", "leetcode"))