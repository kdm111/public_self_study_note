class Solution:
    def arrangeCoins(self, n: int) -> int:
        # sol1 O(1), O(1) 32~62ms 98~57%  
        # sol = (-1 + (1 + 4*2*n)**0.5) / 2
        # return int(sol)


        # sol2 O(logn), O(1) 50~81ms 72~47% 
        left, right = 0, n
        while left <= right:
            mid = (left+right)//2
            k = mid*(mid+1)//2
            if k == n:
                return mid
            if k < n:
                left = mid+1
            else:
                right = mid-1
        return right       




print(Solution().arrangeCoins(5))