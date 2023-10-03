class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sol1 O(n) 830ms 5%
        count = {}
        max_count = start = result = 0
        for end in range(len(s)):
            print(count)
            count[s[end]] = count.get(s[end], 0) + 1
            max_count = max(max_count, count[s[end]])
            # end-start+1 window size
            if end - start + 1 - max_count > k:
                count[s[start]] -= 1
                start += 1
            print(result, end-start+1)
            result = max(result, end - start + 1)
        return result

print(Solution().characterReplacement("ABAB", 2))