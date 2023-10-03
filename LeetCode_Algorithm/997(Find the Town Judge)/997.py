class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # 998ms 38% 18.9MB 90%
        arr = [0] * (n+1)
        for [i, j] in trust:
            arr[i] -= 1
            arr[j] += 1
        for i in range(1, n+1):
            if arr[i] == n-1:
                return i
        return -1