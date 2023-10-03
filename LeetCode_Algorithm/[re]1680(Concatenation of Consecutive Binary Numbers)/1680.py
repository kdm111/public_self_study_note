class Solution:
    def concatenatedBinary(self, n: int) -> int:
        # sol1 time limit exceeded
        # total = ""
        # for num in range(1, n+1):
        #     temp = ""
        #     while num > 0:
        #         if num & 1:
        #             temp += '1'
        #         else:
        #             temp += '0'
        #         num = num >> 1
        #     total += "".join(list(reversed(list(temp))))
        # i = 1; ans = 0
        # for idx in range(len(total)-1, -1, -1):
        #     if total[idx] == '1':
        #         ans += i
        #     i *= 2
        # return ans % (10 ** 9 + 7)


        # sol2 time limit exceeded
        # 각 숫자마다 n의 시간 복잡도를 가지며 n개가 필요하므로
        # O(n^2) 
        # ans = 0; i = 1
        # for num in range(n, 0, -1):
        #     while num > 0:
        #         if num & 1:
        #             ans += i
        #         num = num >> 1
        #         i *= 2
        # return ans % (10 ** 9) + 7

        # sol3 2750ms 49%
        # O(nlogn) O(n)
        mod = (10 ** 9)+7
        ans = ""
        ans += "".join(bin(i)[2:] for i in range(n+1))
        return int(ans, 2) % mod

        # sol4 time limit exceeded
        # binary = []
        # for num in range(1, n+1):
        #     temp = []
        #     while num > 0:
        #         temp.append(num & 1)
        #         num = num >> 1
        #     binary.extend(list(reversed(temp)))
        # ans = 0; power = 0
        # for i in range(len(binary)-1, -1, -1):
        #     if binary[i] & 1:
        #        ans +=  2 ** power
        #        ans = ans % (10**9+7)
        #     power += 1
        # return ans
        


        
print(Solution().concatenatedBinary(3))
print(Solution().concatenatedBinary(12))

                    
