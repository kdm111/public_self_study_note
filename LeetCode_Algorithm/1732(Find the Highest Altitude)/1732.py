class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        # sol1 44ms 38% 16.3MB 22%
        ans = 0; temp = 0
        for num in gain:
            temp += num
            ans = max(ans, temp)
        return ans

        # sol2
        return max(accumulate([0] + gain))
        