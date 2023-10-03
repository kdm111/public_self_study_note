from typing import List
'''
LeetCode 1706 Where Will the Ball Fall
그리드가 주어질 때 위에서 공이 떨어진다고 가정 공은 어느 곳으로 떨어질 것인가

sol1 T : 369ms 69% S : 14.3MB 84%
T : O(mn) S : O(1)
일단 모든 공의 개수를 ans에 저장
가는 방향을 따라서 공을 내리면서 공의 col을 바꿔가면서 진행
진행 방향의 위를 체크하는 데 그 위는 내가 진행한 방향과 같아야 함 다르면 같힌 공으로 인식
'''
class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        # sol1
        ans = [i for i in range(len(grid[0]))]
        for c in range(len(grid[0])):
            for r in range(len(grid)):
                temp = grid[r][ans[c]]
                ans[c] += grid[r][ans[c]]
                if ans[c] < 0 or ans[c] >= len(grid[0]):
                    ans[c] = -1
                    break;
                if grid[r][ans[c]] != temp:
                    ans[c] = -1
                    break ;
        return ans



print(Solution().findBall([[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]))
print(Solution().findBall([[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]))
print(Solution().findBall([[1]]))

