from typing import List
'''
LeetCode 888 : Fair Candy Swap

앨리스와 밥은 각각 캔디 박스를 가지고 있고 
한 박스만 교환해서 각자 갖고 있는 캔디 수를 맞춰라
답은 단 하나이며 존재한다.

sol1 time limit exceeded
방정식을 구하면 쉽게 풀수 있는 문제이다.
A는 앨리스의 합, B는 밥의 합이다.
A - x + y  = B + x - y
이므로 y를 구하고자 하면
2y = B - A + 2x
y = (B-A) / 2 + x가 된다.

sol2 1052ms 28% 16% 37%
사이즈 시간 초과가 떴으므로 bobSize를 set으로 초기화한다.
'''
class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        
        aliceSum = sum(aliceSizes); bobSum = sum(bobSizes)
        diff = bobSum - aliceSum
        bobSizes = set(bobSizes)
        for x in aliceSizes:
            if (x + (diff) / 2) in bobSizes:
                return [x, int(x + diff / 2)]
        pass

print(Solution().fairCandySwap([1,1], [2,2]))