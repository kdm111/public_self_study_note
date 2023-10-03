'''
LeetCode 78 : Subsets
주어진 숫자 리스트에서 만들 수 있는 모든 서브셋을 리턴하라

# sol1 36ms 82% 14MB 83%
O(n * 2^n) O(n * 2^n)
simple dfs


'''
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        self.ans = []
        self.solve(nums, 0, [])
        return self.ans
    def solve(self, nums, idx, temp):
        self.ans.append(temp[:])
        for i in range(idx, len(nums)):
            temp.append(nums[i])
            self.solve(nums, i+1, temp)
            temp.pop()

print(Solution().subsets([1,2,3]))
