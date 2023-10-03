from typing import List
'''
LeetCode 1512 Number of Good Pairs
넘버 배열이 들어올 때  굿 페어의 경우의 수
굿 페어란 배열에서 두 인덱스의 숫자가 같고 인덱스가 차이가 날  경우 굿 페어라고 한다.
이전에 있었던 인덱스를 모두 포함한다.
[1,1,1]에서 굿 페어의 수는 (0,1), (0,2), (1,2)이다.

sol1 T : 67ms 39% S: 13.9MB 12%
T : O(n) S : O(n)
나오는 숫자들을 카운트할 배열을 만들고 카운트 하면서 카운트를 더한다.
'''
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # sol1
        cntArr = [0] * 101; ans = 0
        for num in nums:
            ans += cntArr[num]
            cntArr[num] += 1
        return ans
print(Solution().numIdenticalPairs([1,2,3,1,1,3]))
        