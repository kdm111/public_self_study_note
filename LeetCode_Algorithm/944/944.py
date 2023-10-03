from tempfile import tempdir
from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # sol1 154~253ms 78~37%
        if len(strs) == 1:
            return 0
    
        cnt = 0
        for c in range(len(strs[0])):
            for r in range(len(strs)-1):
                if strs[r][c] > strs[r+1][c]:
                    cnt += 1 
                    break
        return cnt


print(Solution().minDeletionSize(["zyx","wvu","tsr"]))