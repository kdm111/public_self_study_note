'''
LeetCode 486 :  Predict the Winner
플레이어가 번갈아 가며 배열의 제일 처음과 제일 끝을 뽑는다.
플레이어 1이 이길 수 있다면 true를 반환하고 이길 수 없다면 false를 반환하라.
'''


class Solution:
    def PredictTheWinner(self, nums: list[int]) -> bool:
        return self.solve([], [], nums, True)
    def solve(self, player1, player2, nums, turn):
        if len(nums) == 0:
            print(player1, player2)
            if sum(player1) > sum(player2):
                return True
            else:
                return False
        if turn:
            return self.solve(player1+[nums[0]], player2, nums[1:], False) or self.solve(player1+[nums[-1]], player2, nums[0:len(nums)-1], False)

        else:
            return self.solve(player1, player2+[nums[0]], nums[1:], True) or self.solve(player1, player2+[nums[-1]], nums[0:len(nums)-1], True)

print(Solution().PredictTheWinner([1,5,2]))
