'''
LeetCode 2351 : First Letter to Appear Twice
주어진 문자열에서 첫 번째로 두 번 나타나는 글자 구하기

# sol1 31ms 79% 13.8MB 94%
O(n) O(n)
set에 넣어놓고 체크
'''
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        check = set()
        for c in s:
            if c in check:
                return c
            check.add(c)
        