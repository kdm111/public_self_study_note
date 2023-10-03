from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # sol1
        # 260~282ms 44~30%
        # for i in range(len(flowerbed)):
        #     prev, prevCheck = i-1, 0
        #     next, nextCheck = i+1, 0

        #     if flowerbed[i] == 1:
        #         continue
        #     if prev < 0: prevCheck = 1
        #     if next >= len(flowerbed): nextCheck = 1
        #     if 0 <= prev < len(flowerbed):
        #         if flowerbed[prev] == 0:
        #             prevCheck = 1

        #     if 0 <= next < len(flowerbed):
        #         if flowerbed[next] == 0:
        #             nextCheck = 1

        #     if prevCheck and nextCheck:
        #         flowerbed[i] = 1
        #         n -= 1
        # return True if (n<=0) else False


        # sol2 O(n)
        # 179ms 14% 14.3MB 63%
        def emptyLeft(idx):
            return idx == 0 or flowerbed[idx - 1] == 0
        def emptyRight(idx):
            return idx == len(flowerbed)-1 or flowerbed[idx + 1] == 0
        for i in range(len(flowerbed)):
            if n == 0:
                return True
            if flowerbed[i] == 0 and emptyLeft(i) and emptyRight(i):
                flowerbed[i] = 1
                n -= 1
        return n == 0
    
print(Solution().canPlaceFlowers([0,0,1,0,0], 1))
            
