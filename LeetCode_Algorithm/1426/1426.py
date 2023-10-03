from typing import List

class Solution:
    def countElements(self, arr: List[int]) -> int:
        # sol1 O(n) 79ms~104ms 17~6%
        # hashMap = {}
        # for num in arr:
        #     if num not in hashMap:
        #         hashMap[num] = 1
        #     else:
        #         hashMap[num] += 1

        # ans = 0
        # visited = []
        # for idx in range(len(arr)):
        #     if arr[idx] not in visited:
        #         visited.append(arr[idx])
        #         if arr[idx] in hashMap:
        #             if arr[idx]+1 in hashMap:
        #                 ans += hashMap[arr[idx]]
        # return ans


        # sol2 O(n) 40ms 89%
        # hashMap = set(arr)
        # ans = 0
        # for num in arr:
        #     if num+1 in hashMap:
        #         ans += 1
        # return ans

        # sol3 O(nlogn) 34ms 97%
        # arr.sort()
        # ans = 0
        # length = 0
        # for i in range(len(arr)):
        #     if arr[i-1] != arr[i]:
        #         if arr[i-1] == arr[i]-1:
        #             ans += length;
        #         length = 0
        #     length += 1
        # return ans


        # sol4 O(n^2) 107ms 7%
        # ans = 0
        # for num in arr:
        #     if num+1 in arr:
        #         ans += 1
        # return ans

        # sol5 O(n) O(n)
        cnt = [0] * len(arr)
        for n in arr:
            cnt[n] += 1
        for c in cnt:
            if c != 1:
                return 0
        return len(cnt)
        
print(Solution().countElements([1,1,2,2]))
print(Solution().countElements([1,2,3]))
print(Solution().countElements([1,1,3,3,5,5,7,7]))
