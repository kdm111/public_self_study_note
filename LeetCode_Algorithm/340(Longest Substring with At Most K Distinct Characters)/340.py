class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        # sol1 120ms 56%
        # O(n) O(k)
        if len(s) < k+1:
            return len(s)
        from collections import defaultdict
        hashMap = defaultdict()
        left = 0; right = 0; ans = 0
        while right < len(s):
            hashMap[s[right]] = right
            if len(hashMap) == k+1:
                val = min(hashMap.values())
                hashMap.pop(s[val])
                left = val+1
            ans = max(ans, right-left+1)
            right += 1
        return ans            

print(Solution().lengthOfLongestSubstringKDistinct("eceba", 2))
print(Solution().lengthOfLongestSubstringKDistinct("abcabcabc", 2))

