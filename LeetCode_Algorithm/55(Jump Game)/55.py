'''
LeetCode 55 : Jump Game
주어진 배열에서 마지막 인덱스에 도달할 수 있으면 참 아니면 거짓
주어진 숫자는 점프할 수 있는 최대 맥시멈 점프 길이이다.

# sol1 time limit exceeded
brute force
O(2^n) O(n)
주어진 점프 길이가 최대 인 점을 이용하여 모든 것을 찾아낸다.

# sol2  time limit exceeded
O(n^2) O(n)
dp를 이용해서 계산하되 정해진 길이를 반복하며 재귀로 돈다.
True를 만나면 끝나므로 시간복잡도는 O(n^2)이다.

# sol3 5092ms 6% 15.3MB 18%
O(n^2) O(n)
뒤에서 부터 만나고 True를 만나면 바로 깨진다.

# sol4 458ms 98% 15.1MB 82%
현재 자리에서 goal을 넘어서 도달할 수 있다면 
goal을 현재 idx에 저장한다.


'''

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        # sol1
    #     return self.solve(0, nums)
        # sol2
        # self.dp = [None] * len(nums)
        # self.dp[-1] = True
        # return self.solve2(0, nums)

        # sol3
        # dp = [None] * len(nums)
        # dp[-1] = True
        # for i in range(len(nums)-1, -1, -1):
        #     canJump = min(len(nums)-1, i+nums[i])
        #     for j in range(i+1, canJump+1):
        #         if dp[j] == True:
        #             dp[i] = True
        #             break
        # return dp[0] == True

        # sol4
        goal = len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            if nums[i] + i >= goal:
                goal = i
        return goal == 0
            

    # def solve2(self, idx, nums):
    #     if self.dp[idx] != None:
    #         return self.dp[idx] == True
    #     size = min(idx+nums[idx], len(nums)-1)
    #     for i in range(idx+1, size+1):
    #         if self.solve2(i, nums):
    #             self.dp[idx] = True
    #             return True
    #     self.dp[idx] = False
    #     return False
        
        
            
    # def solve1(self, idx, nums):
    #     if idx == len(nums)-1:
    #         return True
    #     if idx >= len(nums):
    #         return False
    #     for i in range(idx+1, idx+nums[idx]+1):
    #         if self.solve(i, nums):
    #             return True
    #     return False

# print(Solution().canJump([2,3,1,1,4]))
print(Solution().canJump([3,2,1,0,4]))
# print(Solution().canJump([2,0]))
# print(Solution().canJump([0,2,3]))

# print(Solution().canJump([0,1]))

'''
3 2 1 0 4
T T T T


'''