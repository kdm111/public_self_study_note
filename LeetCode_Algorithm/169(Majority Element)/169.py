from typing import List
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # sol1 O(n), O(n) 168~203ms 93~64%
        # hashMap = {}
        # for num in nums:
        #     if num in hashMap:
        #         hashMap[num] += 1
        #     else:
        #         hashMap[num] = 1

        # for key in hashMap:
        #     if hashMap[key] > len(nums)//2:
        #         return key

        # sol1-1
        # collections 모듈의 Counter
        # counts = Counter(nums)
        # return max(counts.keys(), key=counts.get)

        # sol2
        # key는 항상 n//2이상 존재하므로 
        # 정렬한 뒤 nums[n//2]를 찾는다.
        # nums.sort()
        # return nums[len(nums)//2]

        # sol3 O(n^2) O(1) 시간 초과
        for num in nums:
            count = sum (1 for elem in nums if elem == num)
            if count > len(nums)//2:
                return num




print(Solution().majorityElement([5,6,6]))