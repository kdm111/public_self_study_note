'''
Leetcode 2352 : Equal Row and Column Pairs
n * n grid이 주어졌을 때 가로 줄과 세로줄의 요소들이 같은 개수를 리턴하라.

# sol1 817ms 44% 19.3MB 12%
줄을 묶어서 해시맵에 저장 뒤 카운트

'''
class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        # sol1
        rows = {}
        for r in range(len(grid)):
            if self.setKey(grid[r]) not in rows:
                rows[self.setKey(grid[r])] = 1
            else:
                rows[self.setKey(grid[r])] += 1
        ans = 0
        for c in range(len(grid[0])):
            temp = []
            for r in range(len(grid)):
                temp.append(grid[r][c])
            if self.setKey(temp) in rows and rows[self.setKey(temp)] >= 1:
                ans += rows[self.setKey(temp)]
        return ans
    def setKey(self, arr):
        key = ""
        for num in arr:
            key += str(num) + ','
        return key


