import enum


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        # sol1 824ms 20%
        n = len(s)
        if n < 3:
            return n

        left = right = 0
        from collections import defaultdict
        hashMap = defaultdict()
        ans = 2
        while right < n:
            hashMap[s[right]] = right
            if len(hashMap) == 3:
                del_idx = min(hashMap.values())
                hashMap.pop(s[del_idx])
                left = del_idx + 1
            ans = max(ans, right - left+1)
            right += 1

        return ans

# print(Solution().lengthOfLongestSubstringTwoDistinct("eceba"))
# print(Solution().lengthOfLongestSubstringTwoDistinct("cdaba"))
# print(Solution().lengthOfLongestSubstringTwoDistinct("ccaabbb"))
print(Solution().lengthOfLongestSubstringTwoDistinct("abcabcabc"))

