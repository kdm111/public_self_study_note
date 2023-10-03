from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        # sol1 two hashMap 65~75ms 20~9%
        # hash_map = {}
        # for num in arr:
        #     if num not in hash_map:
        #         hash_map[num] = 1
        #     else:
        #         hash_map[num] += 1
        # count_map = {}
        # for (k,v) in hash_map.items():
        #     if v not in count_map:
        #         count_map[v] = 1
        #     else:
        #         return False
        # return True

        # sol2 67~111ms 17~5%
        # count = []
        # for num in arr:
        #     count.append(arr.count(num))
        # return (len(set(count)) == len(set(arr)))

        # sol3 57ms 19% 16.6MB 20%
        hashMap = {}
        for num in arr:
            if num in hashMap:
                hashMap[num] += 1
            else:
                hashMap[num] = 1
        cnt = set()
        for [_, v] in hashMap.items():
            cnt.add(v)
        return len(cnt) == len(set(arr))
            
        
print(Solution().uniqueOccurrences([1,2,2]))