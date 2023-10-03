'''
LeetCode 2206 : Divide Array Into Equal Pairs
배열을 2*len(arr)개의 페어로 나눌 수 있는지 확인하라
페어에는 동일한 요소 2개가 들어간다.

# sol1 95ms 91% 14.3MB 19%
O(n) O(n)
해쉬맵으로 체크

# sol2 93ms 93% 14MB 61%
set으로 체크
'''
from typing import List
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        # sol1
        # from collections import defaultdict
        # hashMap = defaultdict(int)
        # for num in nums:
        #     if hashMap[num] > 0:
        #         hashMap[num] -= 1
        #     else:
        #         hashMap[num] += 1
        # for key in hashMap:
        #     if hashMap[key] != 0:
        #         return False
        # return True

        # sol2
        hashSet = set()
        for num in nums:
            if num in hashSet:
                hashSet.discard(num)
            else:
                hashSet.add(num)
        return len(hashSet) == 0

print(Solution().divideArray([3,2,3,2]))
