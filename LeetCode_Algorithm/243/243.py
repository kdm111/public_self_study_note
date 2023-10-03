from typing import List

class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        # sol1 O(n), O(1) 72~121ms 81~19% 
        ans = 999999999
        word1_idx = -1; word2_idx = -1; 
        for idx in range(len(wordsDict)):
            if wordsDict[idx] == word1:
                word1_idx = idx
            elif wordsDict[idx] == word2:
                word2_idx = idx
            # print(word1_idx, word2_idx)
            if word1_idx >= 0 and word2_idx >= 0:
                ans = min(ans, abs(word1_idx-word2_idx))
        return ans
        # sol2 O(n^2), O(1)
        # brute-force
        
        
        


print(Solution().shortestDistance(["practice", "makes", "perfect", "coding", "makes"], "makes", "coding"))