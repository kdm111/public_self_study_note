'''
LeetCode 216 : Combination Sum III
1~9까지의 k의 조합을 구하는 데 
합이 n과 같은 모든 조합을 구하라.

# sol1 24ms 97% 13.9MB 15%
조합을 백트래킹으로 구한 뒤 ans에 복사한다.

'''
class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        ans = []
        def solve(temp, start, totalSum):
            if len(temp) == k and totalSum == n:
                ans.append(temp[:]); return ;
            for num in range(start, 10):
                if totalSum + num <= n:
                    temp.append(num)
                    solve(temp, num + 1, totalSum + num)
                    temp.pop()
                else:
                    break
        solve([], 1, 0)
        return ans

print(Solution().combinationSum3(4, 1))