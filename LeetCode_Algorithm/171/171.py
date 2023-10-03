class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # sol1 O(n), O(1) 44~54ms 60~34%
        # 알파벳으로 이루어진 27진수 숫자를 10진수로 나타내기
        # right to left

        # place_value = 1
        # ans = 0
        # for i in columnTitle[::-1]:
        #     ans += place_value * (ord(i)-64)
        #     place_value *= 26
        # return ans

        # sol2 36~58ms 83~25%
        # left to right
        ans = 0
        alpha_map = {chr(i+65): i+1 for i in range(26)}
        for i in range(len(columnTitle)):
            ans = (ans * 26) + alpha_map[columnTitle[i]]
        return ans

print(Solution().titleToNumber("AB"))