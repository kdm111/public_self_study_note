'''
LeetCode 1356 : Sort Integers by The Number of 1 Bits
정렬 되어 있는 배열이 존재할 때  
그 숫자들을 이진수 1의 오름차순으로 정렬하라.

sol1 T : 1011ms 5% S : 14.1MB 31%
O(nlogn) O(n)
퀵 소트를 쓰고 비교는 cnt함수를 만들어서 1bit의 카운트를 비교하며 사용

sol2 T : 212ms 12% S : 14.3MB 5%
O(nlogn) O(n) 
sol1은 너무 많은 시간이 소모되었다. 
해쉬맵으로 cnt함수 값에 따라 분류하고 각각 sort를 통해 값을 구한다.

sol3 T : 144ms 56% S : 14MB 95%
아직 속도가 많이 나오지는 않는다.
그냥 arr의 숫자들을 꺼내서 동시에 정렬하는 방법
'''
from typing import List
import random
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # sol1
        # return self.quickSort(arr)

        # sol2
        # hashMap = {}
        # for num in arr:
        #     key = self.cnt1Bits(num)
        #     if key not in hashMap:
        #         hashMap[key] = [num]
        #     else:
        #         hashMap[key].append(num)
        # hashMap = sorted(hashMap.items(), key=lambda item : item[0])
        # ans = []
        # for key, arr in hashMap:
        #     sortedArr = sorted(arr)
        #     ans.extend(sortedArr)
        # return ans

        # sol3
        arr.sort(key = lambda num : (sum((num >> i) & 1 for i in range(32)), num))
        return arr
    

    def quickSort(self, arr) -> List[int]:
        if len(arr) <= 1:
            return arr
        mid = random.randint(0, len(arr)-1)
        leftArr = self.quickSort(arr[:mid])
        rightArr = self.quickSort(arr[mid:])
        ret, i, j = [], 0, 0
        while i < len(leftArr) and j < len(rightArr):
            if self.cnt1Bits(leftArr[i]) < self.cnt1Bits(rightArr[j]):
                ret.append(leftArr[i]); i += 1
            elif self.cnt1Bits(leftArr[i]) == self.cnt1Bits(rightArr[j]):
                if self.isAscending(leftArr[i], rightArr[j]):
                    ret.append(leftArr[i]); i += 1
                else:
                    ret.append(rightArr[j]); j += 1
            else:
                ret.append(rightArr[j]); j += 1
        while i < len(leftArr):
            ret.append(leftArr[i]); i += 1
        while j < len(rightArr):
            ret.append(rightArr[j]); j += 1
        return ret

    def cnt1Bits(self, n):
        cnt = 0
        while n > 0:
            if n & 1:
                cnt += 1
            n >>= 1
        return cnt

    def isAscending(self, a, b):
        return a < b

print(Solution().sortByBits([0,1,2,3,4,5,6,7,8]))