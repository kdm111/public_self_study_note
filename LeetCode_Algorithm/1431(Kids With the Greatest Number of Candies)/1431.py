'''
LeetCode 1431 : Kids With the Greatest Number of Candies

# sol1 38ms 75% 13.8MB 95%

'''
class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        max_candies = max(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_candies:
                candies[i] = True
            else:
                candies[i] = False
        return candies