from typing import List
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        # sol1 72ms 39%
        # O(2^n) O(2^n)
        self.ans = set([]); self.n = n;
        for i in range(1,10):
            self.solve(i, k, [])
        return list(self.ans)
    def solve(self, i, k, temp):
        temp.append(i)
        if len(temp) == self.n:
            num = int("".join(str(n) for n in temp))
            self.ans.add(num)
            return ;
        if 0 <= i-k < 10:
            self.solve(i-k, k, temp); temp.pop()
        if 0 <= i+k < 10:
            self.solve(i+k, k, temp); temp.pop()
            
# [101,121,123,210,212,232,234,321,323,343,345,432,434,454,456,543,545,565,567,654,656,676,678,765,767,787,789,876,878,898,987,989]
# [101, 121, 123, 210, 212, 232, 234, 321,323,343,345,432, 434, 454, 456, 543, 545, 565, 567, 654, 656, 676, 678, 765, 767, 787, 789, 876, 878, 898, 987, 989]
print(Solution().numsSameConsecDiff(3,1))

                
            
            