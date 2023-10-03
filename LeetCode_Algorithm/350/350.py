from multiprocessing.connection import answer_challenge
from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # sol1 O(m+n), O(m+n) 60~83ms 71~33% 
        # hashMap
        # 어느 한 배열에서 해쉬맵을 만든다.
        # 다른 배열에서 해쉬맵 값이 1 이상이면 존재하는 것으로 간주한다.

        # hashMap = {}
        # for num in nums1:
        #     if num not in hashMap:
        #         hashMap[num] = 1
        #     else:
        #         hashMap[num] += 1

        # ans = []
        # for num in nums2:
        #     if num in hashMap and hashMap[num] > 0:
        #         hashMap[num] -= 1; ans.append(num) 
        # return ans

        # sol2 O(mlogm+nlogn), O(min(m,n)) 
        # sort
        # 두 어레이를 모두 정렬한다.
        # 두 어레이의 포인터를 각각 두고 
        # 포인터가 가리키는 값을 가리킬 때 까지 계속 증가 시킨다
        # 가리키는 값이 같다면 존재하는 것으로 간주하고 포인터를 한단계씩 올린다.

        nums1.sort(); nums2.sort()
        nums1Idx = 0; nums2Idx = 0
        ans = []
        while nums1Idx < len(nums1) and nums2Idx < len(nums2):
            
            num1 = nums1[nums1Idx]; num2 = nums2[nums2Idx];

            if num1 < num2:
                nums1Idx += 1

            elif num1 > num2:
                nums2Idx += 1

            elif num1 == num2:
                ans.append(num1)
                nums1Idx += 1; nums2Idx += 1

        return ans

print(Solution().intersect([4,9,5], [9,4,9,8,4]))