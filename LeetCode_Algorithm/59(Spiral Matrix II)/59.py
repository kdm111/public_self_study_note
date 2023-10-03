'''
LeetCode 59 : Spiral Matrix II
나선형 배열 만들기

# sol1 24ms 98% 13.8MB 78%
O(n^2) O(n^2)
나선형으로 순회

'''
class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:

        self.ans = [[0] * n for _ in range(n)]
        i = 0; self.val = 1
        while i < n - i:
            self.solve(i, n-i-1)
            i += 1
        return self.ans

    def solve(self, i, k):
        for c in range(i, k+1):
            self.ans[i][c] = self.val
            self.val += 1
        for r in range(i+1, k+1):
            self.ans[r][k] = self.val
            self.val += 1
        for c in range(k-1, i-1, -1):
            self.ans[k][c] = self.val
            self.val += 1
        for r in range(k-1, i, -1):
            self.ans[r][i] = self.val
            self.val += 1


print(Solution().generateMatrix(5))

