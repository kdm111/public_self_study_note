from re import L
from typing import List
class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        # sol1 605ms 87.5%
        # O(mlogm + nlogn)
        # quick sort 후 two pointer
        idx1 = 0; idx2 = 0;
        # slots1.sort(key= lambda x : x[0]); slots2.sort(key=lambda x : x[0])
        slots1= self.quickSort(slots1); slots2 = self.quickSort(slots2)
        while idx1 < len(slots1) and idx2 < len(slots2):
            slot1 = slots1[idx1]; slot2 = slots2[idx2]
            start = max(slot1[0], slot2[0])
            end = min(slot1[1], slot2[1])
            if slot1[1] < slot2[0] or slot2[1] < slot1[0]:
                if slot1[1] < slot2[1]:
                    idx1 += 1
                else:
                    idx2 += 1
                continue
            if end-start >= duration:
                return [start, start+duration]
            if slot1[1] < slot2[1]:
                idx1 += 1
            else:
                idx2 += 1
        return []

    def quickSort(self, arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr)//2]
        less = []; equal = []; greater = []
        for num in arr:
            if num < pivot:
                less.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                greater.append(num)
        return self.quickSort(less)+equal+self.quickSort(greater)

        pass

print(Solution().minAvailableDuration([[10,50],[60,120],[140,210]], [[0,15],[60,70]], 8))
print(Solution().minAvailableDuration([[10,60]], [[12,17],[21,50]], 8))
