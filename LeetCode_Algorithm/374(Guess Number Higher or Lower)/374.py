class Solution:
    def guessNumber(self, n: int) -> int:
        # sol1 24ms 99% 13.9MB 16%
        left, right = 1, n
        while left <= right:
            mid = left + ((right-left) // 2)
            res = guess(mid)
            if res == 0:
                return mid
            elif res == -1:
                right = mid-1
            else:
                left = mid+1