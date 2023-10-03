from tkinter.messagebox import showwarning
from typing import List
class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        # 주어진 어레이에서 k+1개 만큼 개수를 나누고
        # 그 중 최소의 숫자합을 가진 조각을 가져야 하며 내가 가질 수 있는 조각중 최대의 합은?

        # sol1 211ms 98%
        # binary search
        num = k+1
        # 가장 작은 당도, 전체 당도의 평균
        # 답은 두 사이에 존재할 수 밖에 없다.
        left = min(sweetness); right = sum(sweetness) // (k+1)
        while left < right:
            # 두 사이의 평균을 계산한다.
            # 가장 큰 값을 계산해야 하므로 +1을 한다.
            mid = (left+right+1) // 2
            if self.check(sweetness, mid, num):
                left = mid
            else:
                right = mid-1
        return left

    def check(self, sweetness, mid, num):
        cnt = 0; currSum = 0
        for choco in sweetness:
            currSum += choco
            if currSum >= mid:
                cnt += 1; currSum = 0
        if cnt >= num:
            return True
        return False

print(Solution().maximizeSweetness([5,6,7,8,9,1,2,3,4], 8))
print(Solution().maximizeSweetness([1,2,3,4,5,6,7,8,9], 5))


        
            
        