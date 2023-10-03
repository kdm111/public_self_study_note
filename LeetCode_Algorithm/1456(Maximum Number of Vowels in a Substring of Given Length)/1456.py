'''
Leet 1456
# sol1 148ms 51% 17.18MB 62%
O(n) O(1)
하나의 counter안에 모든 모음을 몰아 넣은 다음
k까지 카운트를 한 뒤 추가하고 제거하며 counter를 계산함

'''
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # sol1 O()
        # 200ms 53% 17.3MB 62%
        counter = ('a', 'e', 'i', 'o', 'u')
        ans = 0
        for i in range(k):
            if s[i] in counter:
                ans += 1
        temp = ans
        for i in range(k, len(s)):
            if s[i] in counter:
                ans += 1
            if s[i-k] in counter:
                ans -= 1
            ans = max(ans, temp)
        return ans