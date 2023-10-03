class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # sol1 108ms 5% 16.5MB 15%
        # from collections import defaultdict
        # hashMap = defaultdict()
        # i = 0; ret = 0
        # while i < len(nums):
        #     if nums[i] not in hashMap:
        #         hashMap[nums[i]] = 1
        #     else:
        #         hashMap[nums[i]] += 1
        #     if hashMap[nums[i]] >= 3:
        #         j = i
        #         while j < len(nums) and hashMap.get(nums[j], 0) >= 2:
        #             j += 1
        #         if j < len(nums) and nums[i] != nums[j]:
        #             nums[j], nums[i] = nums[i], nums[j]
        #             ret = j
        #             if nums[i] not in hashMap:
        #                 hashMap[nums[i]] = 1
        #             else:
        #                 hashMap[nums[i]] += 1
        #     i += 1
        # ret = 0
        # for (_, v) in hashMap.items():
        #     ret += min(v, 2)
        # return ret
        
        # sol2 68ms 67% 16.4MB 15%

        # 배열을 조절하면서 뒤에서부터 계산
        ret = len(nums)
        cur = nums[-1]; k = 0
        for i in range(len(nums)-1, -1, -1):
            if cur == nums[i]:
                k += 1
            else:
                k = 1
            if k > 2:
                nums.pop(i)
                nums.append(-1)
                ret -= 1
            cur = nums[i]
        return ret
                
                
      
print(Solution().removeDuplicates([0,0,1,1,1,1,2,3,3]))
print(Solution().removeDuplicates([1,1,1,2,2,3]))
print(Solution().removeDuplicates([1,1,1,1,1]))
print(Solution().removeDuplicates([1,1,1,2,2,2,3,3]))



