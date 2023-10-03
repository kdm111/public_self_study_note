from typing import List

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        # stack sol1 O(n) 49 66
        ans = []
        for chr in ops:
            num = chr.lstrip("-")
            if num.isdigit():
                 ans.append(int(chr))
            elif chr == '+':
                ans.append(ans[-1] + ans[-2])
            elif chr == 'C':
                ans.pop()
            elif chr == 'D':
                ans.append(2 * ans[-1])
        return sum(ans) 



print(Solution().calPoints(["5","-2","4","C","D","9","+","+"]))
