class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # sol1 O(n) O(1) time limit exceeded   
        # low 800445804
        # high 979430543
        # ans = 0
        # while low <= high:
        #     if low % 2 == 1:
        #         ans += 1
        #     low += 1
        # return ans

        # sol2 O(1) O(1) 54ms 28%
        # 짝수와 짝수를 빼면 그 값의 1/2값의 홀수개가 존재한다.
        # low와 high의 범위는 0~ 10^9이다.
        # 0~2 = 1 2~10 = 4
        if low % 2 == 1:
            low -= 1
        if high % 2 == 1:
            high += 1
        return (high-low) // 2

print(Solution().countOdds(3,7))