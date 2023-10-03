from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # sol1 O(mn), O(m+n) 124~194ms 5
        # ans = []
        # nums1 = set(nums1); nums2 = set(nums2)
        # for num1 in nums1:
        #     for num2 in nums2:
        #         if num1 == num2 and num1 not in ans: 
        #             ans.append(num1)

        # return ans
        #  return list(nums2 & nums1)

        # sol2 O(mlogm+nlogn) 65~73ms 57~45%
        # 두 배열을 모두 정렬
        # 두 배열의 인덱스가 가리키는 값이 같다면 ans에 추가하고 인덱스 업데이트
        # 같은 값을 가리키도록 인덱스를 업데이트
        nums1.sort()
        nums2.sort()
        ans = []
        nums1Idx, nums2Idx = 0, 0
        while nums1Idx < len(nums1) and nums2Idx < len(nums2):
            if nums1[nums1Idx] not in ans and nums1[nums1Idx] == nums2[nums2Idx]:
                ans.append(nums1[nums1Idx])
                nums1Idx += 1
            elif nums1[nums1Idx] < nums2[nums2Idx]:
                nums1Idx += 1   
            else:
                nums2Idx += 1

        return ans
                    


print(Solution().intersection([1,1], [1,2]))