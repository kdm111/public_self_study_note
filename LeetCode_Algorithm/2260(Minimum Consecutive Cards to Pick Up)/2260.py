'''
LeetCode 2260 : Minimum Consecutive Cards to Pick Up
정수 배열이 존재할 때 cards[i] 번째는 i번째 카드의 가치를 표현한다. 같은 가치의 카드는 매칭된다.
연속되는 카드매칭이 되는 최소의 숫자를 구하라.
'''
from collections import defaultdict
import sys
class Solution:
    def minimumCardPickup(self, cards: list[int]) -> int:
        cnt = defaultdict(list)
        for i in range(len(cards)):
            cnt[cards[i]].append(i)
        ans = sys.maxsize
        for v in cnt.values():
            for i in range(len(v)-1):
                ans = min(ans, v[i+1]-v[i]+1)

        return -1 if ans == sys.maxsize else ans

