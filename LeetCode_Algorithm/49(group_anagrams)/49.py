import collections
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sol1 O(nklogk) 단어의 길이
        # sorted 192ms 29%
        # hashMap = {}
        # for s in strs:
        #     temp = sorted(list(s))
        #     t = "".join(temp)
        #     if t not in hashMap:
        #         hashMap[t] = [s]
        #     else:
        #         hashMap[t].append(s)
        # ans = []
        # for k, strings in hashMap.items():
        #     ans.append(strings)
        # return ans

        # sol2 O(nk) k는 단어의 길이
        # counting 203ms 22%
        ans = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            if tuple(count) not in ans:
                ans[tuple(count)] = [s]
            else:
                ans[tuple(count)].append(s)
        return ans.values()
            

print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))