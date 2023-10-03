class Solution:
    def climbStairs(self, n: int) -> int:
    # sol1 38에서 시간초과 2^n
    # 38은 63245986
    #     return self.cnt(n)

    # def cnt(self, n):
    #     if n <= 1:
    #         return 1

    #     if n >= 2:
    #         return self.cnt(n-1)+self.cnt(n-2)

    # sol2 memoization n
    # 44~63ms 47~7%보다 빠름
    # 메모이제이션을 활용해서 기존의 값을 이용하여 답을 도출
    #     memory = [0 for _ in range(46)]
    #     memory[1] = 1
    #     memory[2] = 2
    #     return self.cnt(n, memory)

    # def cnt(self, n, memory):
    #     if n <= 0:
    #         return 0;

    #     if memory[n]:
    #         return memory[n]

    #     else:
    #         ways = self.cnt(n-1, memory)+self.cnt(n-2, memory)
    #         memory[n] = ways
    #         return ways

    # sol3 n dp 32~55ms 85~18%보다 빠름
    # n번째 계단을 올라가는 경우의 수는 n-1번째와 n-2번째의 합이다.
    # dp[n] = dp[n-1] + dp[n-2]
        # dp = [0 for _ in range(46)]
        # dp[1] = 1
        # dp[2] = 2
        # if 1 <= n <= 2: return dp[n]

        # for i in range(3, n+1):
        #     dp[i] = dp[i-1]+dp[i-2]

        # return dp[n]

    # sol4 fibonacci O(n)
    # 27~32ms  95~64% 메모리 소모는 큰 차이가 없음..
    # sol3는 공간복잡도가 O(n)이다. 이를 O(1)으로 줄여보자.
    
        # first = 1
        # second = 2
        # if n==1: return 1
        # if n==2: return 2
        # for _ in range(3, n+1):
        #     third = first+second
        #     first = second
        #     second = third
        # return third

    # sol5 recursive
    # 27ms 86% 13.7MB 93%
        if self.dp[n] > 0:
            return self.dp[n]
        self.dp[n] = self.climbStairs(n - 2) + self.climbStairs(n - 1)
        return self.dp[n]
    def __init__(self):
        self.dp = [0] * 46
        self.dp[0] = 1
        self.dp[1] = 1
        self.dp[2] = 2
    




    
        


print(Solution().climbStairs(3))