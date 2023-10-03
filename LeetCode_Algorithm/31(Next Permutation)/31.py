from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # sol1 gerneral permutation O(n!)
        # temp = nums[:]
        # temp.sort()
        # self.permutation = []; self.visited = [False] * len(nums)
        # self.makePermutation(temp,[], 0)
        # for i in range(len(self.permutation)):
        #     if self.checkArray(nums, self.permutation[i]):
        #         if i == len(self.permutation)-1:
        #             nums = self.permutation[0]
        #         else:
        #             nums = self.permutation[i+1]
        #         break
        # return nums

        # sol2 48ms 86%
        # single pass

        # 뒤에서부터 계산하여 내림차순이 되는 포인트를 찾는다.
        i = len(nums)-1
        while i >= 0 and nums[i-1] >= nums[i]:
            i -= 1
        if i < 0: return ;
        # 모든 수가 내림차순으로 되어있을 경우
        if i == 0:
            left = 0; right = len(nums)-1
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1; right -= 1
            return nums
        # 포인트를 찾을 경우 그 시작점부터 그 수보다 큰 수를 찾는다.
        i -= 1; j = len(nums)-1
        while j >= i and nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        # i+1부터 역순으로 정렬한다.
        left = i+1; right = len(nums)-1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1; right -=1
        return nums

    def checkArray(self, arr1, arr2):
        for i in range(len(arr1)):
            if arr1[i] != arr2[i]:
                return False
        return True

    def makePermutation(self, temp, res, idx):
        if len(temp) == len(res):
            self.permutation.append(res[:])
            return ;
        for i in range(len(temp)):
            if self.visited[i] == True:
                continue
            self.visited[i] = True; res.append(temp[i])
            self.makePermutation(temp, res, idx+1)
            self.visited[i] = False; res.pop()

        
print(Solution().nextPermutation([1,3,2]))