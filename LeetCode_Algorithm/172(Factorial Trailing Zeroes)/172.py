'''
LeetCode : 172 :  Factorial Trailing Zeroes


# sol1 7889ms 9% 89.3MB 5%
미리 저장해 놓은 뒤 꺼내서 계산

# sol2 39ms 94% 16.1MB 93%
미리 계산해 놓은 결과를 확인한다.
0~4 : 0
5~9 : 1
10~14 : 2
15~19 : 3
20~24 : 4
25~29 : 6
30~34 : 7
35~39 : 8
40~44:  9
45~49 : 10
50~54 : 12

숫자를 보면 결국 5의 개수를 계산하는 것과 같다. 
2*5가 곱해지면 뒤에 붙는 0이 생길 수 밖에 없다.
따라서 5의 개수를 소인수 분해로 세는 것이다.



'''
dp  = [0] * 10001
dp[0] = 1
class Solution:
    def trailingZeroes(self, n: int) -> int:
        # sol1
        # for i in range(1, n+1):
        #     if dp[i] == 0:
        #         dp[i] = i * dp[i-1]
        # ans = 0; temp = dp[n]
        # while temp % 10 == 0:
        #     ans += 1
        #     temp //= 10
        # return ans

        # sol2
        ans = 0
        while n // 5 != 0:
            ans += n // 5
            n //= 5 
        return ans

print(Solution().trailingZeroes(50))