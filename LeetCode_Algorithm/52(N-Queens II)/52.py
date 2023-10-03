'''
LeetCode 52 N-Queens 2

sol1 T : 92ms 58% S : 13.8MB 80%
T : O(n!) S : O(n)
배열을 만들고 그 안에 가능한 col의 숫자를 넣는다.
'''
class Solution:
    def totalNQueens(self, n: int) -> int:
        self.arr = [0] * n; self.ans = 0
        self.dfs(0)
        return self.ans
    def dfs(self, idx):
        if idx == len(self.arr):
            self.ans += 1
            return ;
        for i in range(1, len(self.arr)+1):
            if self.checkValid(idx-1, i):
                self.arr[idx] = i
                self.dfs(idx + 1)
                self.arr[idx] = -1

    def checkValid(self, idx, i):
        check = 1
        while idx >= 0:
            if self.arr[idx] == i + check:
                return False
            if self.arr[idx] == i - check:
                return False
            if self.arr[idx] == i:
                return False
            check += 1
            idx -= 1
        return True

print(Solution().totalNQueens(10))
            