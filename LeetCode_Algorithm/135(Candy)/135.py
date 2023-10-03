class Solution:
    def candy(self, ratings: list[int]) -> int:
        # sol1 172ms 62% 19.5MB 19%
        n = len(ratings)
        left = [1] * n; right = [1] * n
        for l in range(1, n):
            if ratings[l] > ratings[l-1]:
                left[l] = left[l-1] + 1
        for r in range(n-2, -1, -1):
            if ratings[r] > ratings[r+1]:
                right[r] = right[r+1] + 1
        ans = 0
        for i in range(n):
            ans += max(left[i], right[i])
        return ans

print(Solution().candy([1,0,2]))
print(Solution().candy([1,2,2]))
print(Solution().candy([1,2,3]))
print(Solution().candy([3,2,1]))
print(Solution().candy([0,4,4,5,2,1]))




            