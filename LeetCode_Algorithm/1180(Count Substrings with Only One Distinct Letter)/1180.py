'''
LeetCode 1180 : Count Substrings with Only One Distinct Letter
다음의 규칙을 따르는 총 서브스트링 개수 구하기
a: 1
aa: 3
aaa: 6
aaaa : 10 ...

# sol1 29ms 95% 13.8MB 66%
O(n) O(1)
등차수열로 올라가므로 이전 값과 비교해서 맞으면 1을 더한다.


'''
class Solution:
    def countLetters(self, s: str) -> int:
        ans = 1; cnt = 1
        for i in range(1, len(s)):
            if s[i-1] != s[i]:
                cnt = 1
            else:
                cnt += 1
            ans += cnt
        return ans


