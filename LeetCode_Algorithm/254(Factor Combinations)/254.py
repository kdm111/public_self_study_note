from typing import List
class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        # sol1 time limit exceeded
    #     self.ans = []
    #     self.solve(2, n, [])
    #     return self.ans
    # def solve(self, k, num, arr):
    #     if num == 1 and len(arr) > 1:
    #         self.ans.append(arr); return ;
    #     for i in range(k, num+1):
    #         if num % i == 0:
    #             arr.append(i)
    #             self.solve(i, num//i, arr[:])
    #             arr.pop()

        # sol2 108ms 89%
        self.ans = [];
        self.solve(n, [])
        return self.ans
    def solve(self, n, arr):
        import math
        if arr:
            self.ans.append(arr+[n])
        for k in range(2, int(math.sqrt(n))+1):
            if n % k == 0:
                if arr and k < arr[-1]:
                    continue
                self.solve(n//k, arr+[k])




    
print(Solution().getFactors(12))
print(Solution().getFactors(8))
print(Solution().getFactors(37))

