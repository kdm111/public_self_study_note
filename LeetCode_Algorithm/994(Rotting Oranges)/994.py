from typing import List
class Solution:
    def __init__(self):
        self.minute = 0
        self.dr = [0,1,0,-1]
        self.dc = [1,0,-1,0]
        self.rotten_orange = []
        self.fresh_orange = 0
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # O(n) O(1) 97ms 26%
        # 먼저 오렌지 개수와 썩은 오렌지 위치를 계산
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    self.fresh_orange += 1
                elif grid[r][c] == 2:
                    self.rotten_orange.append([r,c])
        while True:
            temp = []
            while self.rotten_orange:
                r,c = self.rotten_orange.pop(0)
                for i in range(4):
                    new_r = r + self.dr[i]; new_c = c + self.dc[i]
                    if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]):
                        if grid[new_r][new_c] == 1:
                            self.fresh_orange -= 1;
                            grid[new_r][new_c] = 2; temp.append([new_r,new_c])
            self.minute += 1
            if not temp:
                break
            self.rotten_orange = temp
        if self.fresh_orange > 0: return -1
        return self.minute-1 # 가장 마지막에 썩는 과일 체크 시간 제거
            


print(Solution().orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
print(Solution().orangesRotting([[1,2]]))

