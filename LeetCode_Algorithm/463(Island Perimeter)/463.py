'''
LeetCode 463 : Island Perimeter
주어진 섬의 둘레를 구하기

#  sol1 811ms 74% 14.2MB 75%
O(mn) O(1)
dfs를 사용할 경우 공간복잡도가 커지기 때문에 일반 이중 반복문을 사용한다.
섬의 땅일 경우 4에서 그 주위의 섬의 개수를 뺀다.
'''
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                cnt = 4
                if grid[r][c] == 1:
                    for [i,j] in [[0,1], [1,0], [0,-1], [-1,0]]:
                        if 0 <= r + i < len(grid) and 0 <= c + j < len(grid[0]):
                            if grid[r+i][c+j] == 1:
                                cnt -= 1
                    ans += cnt
        return ans