'''

LeetCode 1710 : Maximum Units on a Truck

# sol2 144ms 98% 14.3MB 98%
O(nlogn) O(n)
가장 많이 들어가는 박스부터 싣는다.
일단 한 박스에 들어가는 유닛을 내림차순하고 
현재 트럭 사이즈와 갖고 있는 박스 중 가장 작은 값을 계산하여 
제품 개수 * 가장 작은 값을 답에 저장하고
가장 작은 값을 트럭의 자리에 뺀다.

'''
from typing import List

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # sol1 O(n^2),O(1) 1447~1869ms 9~7%(sol1)
        #                   222~229ms 53~50%
        # 가장 많이 들어가는 박스부터 차례로 싣는다.
        boxTypes.sort(key = lambda box : -box[1])
        # boxTypes.sort(key = lambda box : box[1], reverse=True)
        units = 0
        for boxNum, unit in boxTypes:
            # sol1
            # while boxNum != 0 and truckSize != 0:
            #     boxNum -= 1
            #     units += unit
            #     truckSize -= 1

            # sol1-2
            boxCount = min(boxNum, truckSize)
            units += (unit * boxCount)
            truckSize -= boxCount
            if truckSize == 0:
                break
        return units

        # sol2
        boxTypes.sort(key= lambda x : x[1], reverse= True); ans = 0
        for [boxNum, units] in boxTypes:
            temp = min(boxNum, truckSize)
            ans += units * temp
            truckSize -= temp
            if truckSize == 0:
                break
        return ans


print(Solution().maximumUnits([[5,10],[2,5],[4,7],[3,9]], 10))