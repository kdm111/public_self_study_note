import enum
from typing import List
class Solution:
    def __init__(self, w: List[int]):
        # sol1 9098ms 5%
        # 숫자들이 존재할 때 인덱스 랜덤 픽
        # 단 인덱스에 속한 가중치를 계산해야 한다.
        self.prefix_sums = []
        prefix_sum = 0
        for weight in w:
            # 숫자들을 하나씩 다 더하면서 계산한다.
            prefix_sum += weight
            # 그리고 지금까지 계산값을 하나씩 리스트에 넣는다.
            self.prefix_sums.append(prefix_sum)
        # 최종합은 따로 저장한다.
        self.total_sum = prefix_sum

    def pickIndex(self) -> int:
        import random
        # 최종합에 random을 써서 0~1까지의 수를 랜덤하게 뽑음
        target = self.total_sum * random.random()
        # run a linear search to find the target zone
        for i, prefix_sum in enumerate(self.prefix_sums):
            # 타겟이 그 인덱스의 값보다 더 작으면 인덱스를 리턴
            if target < prefix_sum:
                return i
sol = Solution([1,2])
print(sol.prefix_sums)
print(sol.pickIndex())
print(sol.pickIndex())
print(sol.pickIndex())
print(sol.pickIndex())

print(sol.pickIndex())
