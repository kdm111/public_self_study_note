'''
leetCode : 1208
s 문자열이 t 문자열이 되는 비용은 두 문자의 ascii 차의 값이다.
maxCost를 사용하여 가장 길게 만들 수 있는 문자열을 구하라.

# sol1 76ms 60% 17.08MB 83.3%
각 문자마다 차이를 뺀 뒤 가능한 문자열의 길이를 구한뒤 max길이를 체크한다.

'''
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        i = j = 0; ans = 0
        while j < len(s):
            maxCost -= abs(ord(s[j]) - ord(t[j]))
            while maxCost < 0:
                maxCost += abs(ord(s[i]) - ord(t[i]))
                i += 1
            j += 1
            ans = max(ans, j - i)
        return ans

print(Solution().equalSubstring("abcd", "bcdf", 3))
print(Solution().equalSubstring("abcd", "cdef", 3))
print(Solution().equalSubstring("abcd", "acde", 0))
print(Solution().equalSubstring("krrgw", "zjxss", 19))
print(Solution().equalSubstring("arrgw", "zjxss", 0))



