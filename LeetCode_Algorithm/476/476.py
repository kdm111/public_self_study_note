class Solution:
    def findComplement(self, num: int) -> int:
        # 41ms 50%
        # binary_str = ""
        # while num > 0:
        #     binary_str += str(num % 2)
        #     num //= 2

        # binary_str[::-1]
        # ans = 0
        # for idx in range(len(binary_str)):
        #     if binary_str[idx] == '0':
        #         ans += 2 ** idx
        # return ans

        # sol2 64ms 5%
        # bit = 1
        # while num >= bit:
        #     num = num ^ bit
        #     bit = bit << 1
        # return num

        # sol3 50ms 25%
        return 2 ** num.bit_length() - (1 + num)


        
print(Solution().findComplement(10))
print(Solution().findComplement(5))
print(Solution().findComplement(1))
