'''
LeetCode 740 : Delete and Earn

숫자 배열이 존재할 때 다음과 같은 규칙을 통해서 최대의 점수를 얻고 싶다.
nums[i]가 있을 때 지우고 nums[i]점을 얻는다.
지우는 동시에 모든 nums[i]-1, nums[i]+1점이 사라진다. 점수는 얻지 못한다.
얻는 점수를 최대로 했을 때 얻을 수 있는 점수를 구하라.

# sol1 67ms 62% 14.87MB 92%
cnt 배열을 만들어서 카운트 해야 한다. 각 숫자의 누적을 저장한다.
숫자가 업데이트 되며 이전의 값에 값을 더한뒤 현재와 비교해 더 큰 값을 현재에 저장


'''
class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        # sol1
        cnt = [0] * (max(nums) + 1)
        for num in nums:
            cnt[num] += num
        prev = curr = 0
        for v in cnt:
            prev, curr = curr, max(prev + v, curr)
        return curr

    
# print(Solution().deleteAndEarn([2,4,3]))
print(Solution().deleteAndEarn([2,2,3,3,3,4]))
# print(Solution().deleteAndEarn([1,1,1,2,4,5,5,5,6]))
# print(Solution().deleteAndEarn([1,1,1,2,4]))
# print(Solution().deleteAndEarn([1,3,5,7,9]))
# print(Solution().deleteAndEarn([1,1,2,99]))







