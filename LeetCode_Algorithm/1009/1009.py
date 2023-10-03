from math import floor, log2

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        # sol1 41~56ms 56~16%
        # bin_n = bin(n)
        # ans = 0
        # num = 1
        # for chr in bin_n[::-1]:
        #     if chr == "0":
        #         ans += num 
        #     num *= 2
        # return ans-(num//2)

        # sol2 O(1), O(1) 45 44%
        # n.bit_length()를 통해 최대 비트 길이를 구한뒤
        # 1을 빼면 그 비트가 가지는 최대 숫자가 되고 
        # n을 빼면 부족한 숫자가 나온다.
        # return (1 << n.bit_length()) -1 -n if n else 1

        # sol3
        # bitmask
        # 숫자의 비트 크기는 log의 값을 취한 뒤 1을 더하면 된다.
        # bitmask는 최대 크기까지 1을 채워 넣은 값이다.
        # 최대 크기까지 1을 뺀 뒤에 xor연산을 취한다.
        l = floor(log2(n))+1
        bitmask = (1 << l) -1
        return bitmask ^ n

print(Solution().bitwiseComplement(4))