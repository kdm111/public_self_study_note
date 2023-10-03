'''
LeetCode 405 : Convert a Number to Hexadecimal
10진수를 16진수로 바꾸기
'''
class Solution:
    def toHex(self, num: int) -> str:
        # sol1 25ms 93% 13.7MB 94%
        if num == 0: return "0"
        if num < 0: num += 2 ** 32
        hex = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        ans = ""
        while num != 0:
            ans = hex[num & 15] + ans
            num >>= 4
        return ans


print(Solution().toHex(-1))