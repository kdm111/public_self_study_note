
from turtle import left
import numpy 

class Solution:
    def mySqrt(self, x: int) -> int:
        # sol1 O(1), O(1) 28~32ms 99~98%
        # 내장 함수 사용
        # return int(x ** 0.5)

        # sol1-1
        # x**0.5 사용 금지
        # if x < 2: return x;

        # left = int(numpy.e ** (0.5 * (numpy.log(x))))
        # right = left+1
        # return left if right*right > x else right # 소수점으로 인해 값이 달라질 수 있음 그래서 제곱을 한 뒤 
        #                                           # 원래 값보다 작다면 하나 더 큰 값을 내야 한다.


        # sol2 O(logn), O(1) 222~279ms 20%
        # binary search
        # if x == 1: return x
        # left, right = 1, x
        # while left <= right:
        #     pivot = left + (right-left)//2 
        #     num = pivot*pivot

        #     if num < x:
        #         left = pivot + 1
        #     elif x < num:
        #         right = pivot-1
        #     else:
        #         return pivot

        # return right

        # sol3 O(logn) O(1) 181~220ms 20%
        # bit shift
        # sqrt = x ** 0.5 
        #      = 2 * ((x / 4) ** 0.5))
        # 1에서부터 올라가면서 *2를 해가면서 찾는다. 
        # +1한 값을 체크해서 값이 크다면 -1값을 작다면 +1값을 출력한다.
        if x < 2: return x
        left = self.mySqrt(x >> 2) << 1
        right = left+1
        # print(left, right)
        return left if right*right > x else right
            




print(Solution().mySqrt(99))