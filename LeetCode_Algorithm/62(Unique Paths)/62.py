class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # sol1 O(mn) 39ms 73%
        board = [[1] * n for _ in range(m)]
        for r in range(1, m):
            for c in range(1, n):
                board[r][c] = board[r-1][c] + board[r][c-1]
        return board[m-1][n-1]

        # sol2

        pass


print(Solution().uniquePaths(3,7))