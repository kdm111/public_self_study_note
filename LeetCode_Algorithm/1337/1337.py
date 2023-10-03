class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        # 117ms 50% 14.4MB 9%
        lst = []
        for r in range(len(mat)):
            lst.append((r, mat[r].count(1)))
        lst.sort(key = lambda x : x[1])
        ans = []
        for i in range(k):
            ans.append(lst[i][0])
        return ans

print(Solution().kWeakestRows([[1,1,0,0,0], [1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]], 3))
