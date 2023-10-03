'''
LeetCode 77 : Combinations
nCk를 1...n까지의 수 중에서 k를 만들어라

# sol1 418ms 68% 15.9MB 49%
O(k * n!/ (n-k)! * k!) O(n! / (n-k)! * k!) 
백트래킹을 통한 조합 구하기
'''
class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        self.ans = []
        self.solve(n, k , [], 1)
        return self.ans
    def solve(self, n, k, temp, idx):
        if len(temp) == k:
            self.ans.append(temp[:])
            return ;
        for i in range(idx, n+1):
            temp.append(i)
            self.solve(n, k , temp, i+1)
            temp.pop()
        
print(Solution().combine(4,2))
print(Solution().combine(1,1))
