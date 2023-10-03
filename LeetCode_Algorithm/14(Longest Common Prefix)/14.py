from typing import List

'''
LeetCode 14 Longest Common Prefix
주어진 strs에서 가장 긴 공통 prefix 찾기

sol1 T : 54ms 73% S : 13.8MB 49%
T : O(n) S : O(1)
가장 작은 길이를 찾아 그 길이만큼 비교하면서 다른 글자가 나올 때까지 계산

'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # sol1
        # ans = strs[0] if len(strs) > 0 else ""
        # for str_idx in range(1, len(strs)):
        #     char_idx = 0
        #     while char_idx < min(len(ans), len(strs[str_idx])):
        #         if ans[char_idx] != strs[str_idx][char_idx]:
        #             break
        #         char_idx += 1
        #     ans = ans[0:char_idx]
        # return ans


        # sol2 50ms 59% 16.1MB 99%
        ans = strs[0]
        for i in range(1, len(strs)):
            idx = 0; minLen = min(len(strs[i]), len(ans))
            while idx < minLen and ans[idx] == strs[i][idx]:
                idx += 1
            ans = ans[:idx]
        return ans

    
        
    


            
    
        

print(Solution().longestCommonPrefix(["dog", "fdog", "dog", "fdog", "dog", "fdog"]))
print(Solution().longestCommonPrefix(["dog"]))
