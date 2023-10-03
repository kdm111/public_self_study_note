class Solution:
    def reverseBits(self, n: int) -> int:
        # sol1 66ms 24%
        # bit by bit
        ans = 0; pow = 31
        while n:
            # lsb의 값을 pow값만큼 밀어준 값을 더함
            ans += (n & 1) << pow
            # 1비트만큼 오른쪽으로 이동
            n = n >> 1
            # pow는 감소
            pow -= 1
        return ans

print(Solution().reverseBits(10))