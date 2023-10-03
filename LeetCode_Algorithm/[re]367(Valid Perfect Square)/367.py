class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # sol1 52ms 52%
        # O(logn)
        # l,r을 정해서 그 중간 값을 계속 찾아나감
        # 그 중간 값을 제곱한 값이 같다면 리턴 true
        # 크다면 right를 감소
        if num == 1:
            return True
        left, right = 2, (num // 2) + 1
        while left <= right:
            mid = left + (right - left) // 2
            print(mid)
            if mid ** 2 == num:
                return True
            if mid ** 2 < num:
                left = mid + 1
            else:
                right = mid - 1
        return False

print(Solution().isPerfectSquare(16));