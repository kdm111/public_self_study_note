from gc import isenabled
from typing import List
from xml.dom.minidom import Identified
'''
LeetCode : 561 Array Partition
    # sol1 T : 585ms 49% S : 16.8MB 21%
    T : O(nlogn) S : O(n)(정렬 하는 데 필요한 공간 크기)
    들어온 숫자들을 두 개씩 잘라서 그 min의 합이 최대가 되는 합을 구하기
    소트해서 앞에서 0부터 2만큼 뛰어 넘어 읽어들인다.
'''
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # sol1 
        nums.sort(); ans = 0; i = 0
        while i < len(nums):
            ans += nums[i]
            i += 2
        return ans

                
                
            
        
        
        

print(Solution().arrayPairSum([6,2,6,5,1,2]))