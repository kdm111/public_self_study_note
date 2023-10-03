'''

LeetCode 1304 : Find N Unique Integers Sum up to Zero

n이라는 숫자가 주어질 때 n만큼 길이로 하는 합이 0인 정수 배열을 구하라
단 모든 숫자는 한 번만 쓰인다. (n = 1~1000)

# sol1 51ms 74% 13.9MB 92%
O(1) O(1)
규칙을 생각해보자.
n = 1 [0]
n = 2 [-1, 1]
n = 3 [-1, 0, 1]
n = 4 [-2, -1, 1, 2]
n = 5 [-2, -1, 0, 1, 2]
n = 6 [-3, -2, -1, 1, 2, 3]
n = 7 [-3, -2, -1, 0, 1, 2, 3]
n = 8 [-4, -3, -2, -1, 1, 2, 3, 4]
...

n % 2 == 0일경우 -n/2~ n/2에 해당하는 모든 정수를 추가한 뒤
n % 2 == 1일경우 0을 추가하면 된다.
'''

from typing import List

class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = [-i for i in range(1, n // 2 + 1)] + [i for i in range(1, n // 2 + 1)]
        if n % 2: ans.append(0)
        return ans
print(Solution().sumZero(10))