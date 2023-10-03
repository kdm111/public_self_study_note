'''
LeetCode 1539 : Kth Missing Positive Number
배열이 주어졌을 때 1...n까지의 순에서 k번째 없어진 수를 리턴하라

# sol3 51ms 78% 14MB 44%
첫째항이 k보다 크다면 k를 리턴
첫째항의 -1값을 k에서 제거
배열을 순회하며 각 차이의 -1값을 계산
그 차이가 k보다 더 작다면 k에서 제거
크거나 같다면 k에서 arr[i]+k를 리턴


'''
from typing import List

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # sol1 O(n^2), O(1) 197~298ms 7~5%
        # cnt = 0
        # for i in range(1, 10000):
        #     if i not in arr:
        #         cnt += 1
        #     if cnt == k:
        #         return i

        # sol2  O(n), O(n) 48~124ms 96~12%
        # cnt = [i for i in range(0, arr[0])]
        # if len(cnt) >= k+1:
        #     return cnt[k]

        
        # for i in range(len(arr)-1):
        #     for j in range(1, arr[i+1]-arr[i]):
        #         cnt.append(arr[i]+j)
        #         print(cnt)
        #         if len(cnt) == k+1: return cnt[k]
        # i = 1
        # while True:
        #     cnt.append(arr[-1]+i)
        #     if len(cnt) == k+1: return cnt[k]
        #     i += 1

        # sol3
        if arr[0] > k:
            return k
        k -= arr[0] - 1
        for i in range(len(arr)-1):
            diff = arr[i+1] - arr[i] - 1
            if k <= diff:
                return arr[i] + k
            k -= diff
        return arr[-1] + k

        

        

        

        
print(Solution().findKthPositive([10,20], 11))