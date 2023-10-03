from collections import defaultdict
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        # sol1 O(n), O(n) 143~157ms 82~71%
        # hashmap 
        # hashMap = defaultdict(int) # 정수형 맵으로 초기화
        # for num in nums: 
        #     hashMap[num] += 1

        # for key in hashMap:
        #     if hashMap[key] == 1: return key 

        # sol2 O(n+n), O(n+n) 128~136ms 98~90%
        # set을 활용하여 *2 한 뒤 nums의 합계를 빼줌
        # return 2*sum(set(nums)) - sum(nums)

        # sol3 O(n), O(1) 163~180ms 67~58%
        # bit manipulation
        # a ^ 0 = a
        # a ^ a = 0
        # xor 연산은 같은 수끼리의 연산에서 0이 되고 
        # 0과의 연산에서는 같은 수가 나온다.
        ans = 0
        for num in nums:
            ans ^= num
        return ans


print(Solution().singleNumber([1,2,3,2,1]))

