from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # sol1 m+n 40ms 80%보다 빠름
        # i = m-1
        # j = n-1

        # for idx in range(m+n-1, -1, -1):

        #     if j < 0: break; # j가 nums2를 넘었을 경우 더 이상 비교할 숫자가 없으므로 종료한다.
        #     if i >= 0 and nums1[i] > nums2[j]: # 
        #         nums1[idx] = nums1[i]; i -= 1
        #     else: # i가 nums1을 벗어났을 경우 nums2의 남은 숫자들을 넣는다.
        #         nums1[idx] = nums2[j]; j -= 1
            
        # sol2 100ms 5%보다 빠름
        # nums1의 일부를 복사하여 정렬의 사용하고 원래 배열은 정렬에 사용
        # nums1_copy = nums1[:m]
        # nums1_idx = 0
        # nums2_idx = 0
        # for idx in range(0, m+n):
        #     if nums1_idx >= m or nums2_idx >= n: break;
        #     if nums1_copy[nums1_idx] < nums2[nums2_idx]:
        #         nums1[idx] = nums1_copy[nums1_idx]; nums1_idx += 1;
        #     else:
        #         nums1[idx] = nums2[nums2_idx]; nums2_idx += 1;

        # if nums2_idx < n:
        #     while idx < m+n:
        #         nums1[idx] = nums2[nums2_idx]
        #         idx += 1; nums2_idx += 1

        # if nums1_idx < m:
        #     while idx < m+n:
        #         nums1[idx] = nums1_copy[nums1_idx]
        #         idx += 1; nums1_idx += 1


        # sol3 nlogn 32ms~90ms 97~9%보다 빠름
        # nums1의 빈공간에 nums2를 복사하고 .sort()로 정렬
        
        nums1[m:m+n+1] = nums2[0:n]
        nums1.sort()
             

            


        
        


print(Solution().merge([1,2,3,0,0,0], 3, [2,5,6], 3))


