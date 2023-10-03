'''
    LeetCode 338 : Counting Bits
    0~n까지의 모든 2진 표현의 1의 개수를 배열로 반환
    반복문으로 0~n까지 돌린 다음 이진수로 전환한 다음 
    그 1의 개수를 카운트하여 배열에 넣음
    
    sol1 : bin, count를 통해 계산 : 78% 30%
    sol4 : dp를 이용해 계산
    ans[x + b] = ans[x] + 1; b는 2의 제곱
    위의 식을 계산하면 다음 항을 이전 항의 값을 이용해 계산할 수 있다.
'''
from typing import List
class Solution:
    def countBits(self, n: int) -> List[int]:
        # sol1 T : 129ms 78% S : 20.9% 30%
        # ans = []
        # for num in range(0, n+1):
        #     ans.append(int(bin(num).count('1')))
        # return ans

        # sol2 T : 213ms 36% S : 20.7MB 79%
        # ans = []
        # n_inc = 0
        # while n_inc <= n:
        #     cnt = 0
        #     temp = n_inc
        #     while temp > 0:
        #         if temp & 1:
        #             cnt += 1
        #         temp >>= 1
        #     ans.append(cnt)
        #     n_inc += 1
        # return ans 

        # sol3 T : 198ms 43% S : 21MB 30%
        # O(nlogn) O(1)
        # LSB의 1을 0으로 바꾼 뒤 & 하는 방법
        # ans = [0] * (n + 1)
        # idx = 0
        # for num in range(0, n + 1):
        #     cnt = 0;
        #     while num != 0:
        #         num &= (num - 1)
        #         cnt += 1
        #     ans[idx] = cnt
        #     idx += 1
        # return ans

        # sol4 T : 273ms 22% S : 20.8M 78%
        # dp
        # O(n) O(1)
        ans = [0] * (n + 1)
        num = 0
        b = 1
        while b <= n:
            while num + b <= n:
                ans[num + b] = ans[num] + 1
                num += 1
            # num은 인덱스 역할을 하게된다.
            num = 0
            b <<= 1
        return ans
            
            
# 0 1 2 3 4 5 6 7 8 
# 0 1 1 2 1 2 2 3 1


print(Solution().countBits(5))