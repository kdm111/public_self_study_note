'''
LeetCode 461 : Hamming Distance
주어진 두 정수의 해밍 거리 구하기
해밍 거리 : 주어진 같은 길이의 문자열에서 다른 부분의 길이

# sol1 58ms 41% 13.9MB 13%
비트 연산자로 미루면서 계속해서 and 연산자로 비교함

# sol2 63ms 22% 13.8MB 62% 
bin, count

# sol3 34ms 88% 13.9MB 13%
xor 연산자 비트 쉬프트
'''

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # sol1
        # ans = 0
        # while x != 0 or y != 0:
        #     if x & 1 != y & 1:
        #         ans += 1
        #     x >>= 1
        #     y >>= 1
        # return ans
        # sol2
        return bin(x ^ y).count('1')

        # sol3
        xor = x ^ y; ans = 0
        while xor:
            if xor & 1:
                ans += 1
            xor >>= 1
        return ans

print(Solution().hammingDistance(3, 1))