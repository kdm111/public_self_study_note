from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # sol1 O(n), O(n) 678~972ms 77~26%
        # hashMap
        # 중복된 수끼리의 거리가 k이하일 경우 True를 리턴해야 하는 문제
        # 숫자가 업데이트 될 때마다 인덱스를 해쉬맵 저장하고 
        # 중복 된 숫자가 나올때 k보다 작은지 체크
        # hashMap = {}
        # for idx,num in enumerate(nums):
        #     if num in hashMap:
        #         if idx-hashMap[num] <= k:
        #             return True
        #     hashMap[num] = idx
        # return False


        # sol2 O(n * min(n,k)), O(1) 시간초과(n=59500)
        for i in range(len(nums)):
            j = i+1
            while j < len(nums):
                if i+k < j:
                    break
                if nums[i] == nums[j]: return True
                j += 1
        return False
        
                


        

print(Solution().containsNearbyDuplicate([1,2,3,1,1,2,3], 0))
print(Solution().containsNearbyDuplicate([1,2,3,1], 3))
