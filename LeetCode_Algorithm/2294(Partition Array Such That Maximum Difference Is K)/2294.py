'''
LeetCode 2294 : Partition Array Such That Maximum Difference Is K
주어진 숫자 배열이 있을 때 파티션을 나눌 수 있다.
파티션 안에서 최소값과 최대값의 차이는 최대 k이내 여야 한다. 나눌 수 있는 최소 파티션은 몇 개인가?

# sol1 908ms 79% 28.8MB 36%
숫자를 정렬한 뒤 첫 번째를 저장한다. 
그 첫번째에서 차례로 빼가면서 k보다 커지는 순간 파티션을 하나 추가하고 최소 숫자를 업데이트한다.
'''
class Solution:
    def partitionArray(self, nums: list[int], k: int) -> int:
        # sol1
        nums.sort(); minNum = nums[0]; ans = 1
        for i in range(1, len(nums)):
            if nums[i] - minNum > k:
                ans += 1
                minNum = nums[i]
        return ans

print(Solution().partitionArray([3,6,1,2,5], 2))
print(Solution().partitionArray([2,3], 0))
print(Solution().partitionArray([3,5,6,9], 1))
print(Solution().partitionArray([2,2,4,5], 0))


'''
1 2 3  5 6
'''
