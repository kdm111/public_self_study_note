'''
LeetCode 2073 : Time Needed to Buy Tickets
k번째 숫자가 0이되는 시간을 구하라
티켓은 1초에 1개만 구매할 수 있으며 처음 티켓을 구매하면 뒤로 돌아간다.
걸리는 숫자를 리턴하라

# sol1 108ms 35% 13.9MB 68%
O(k*n) O(1)
티켓을 소모하면서 카운트한다.

# sol2 26ms 99% 13.9MB 68%
O(n) O(1)
k만큼 더해가면서 k보다 인덱스가 크고 tickets[k]보다 큰 수는 -1만큼 더한다.

'''
from typing import List
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # # sol1
        # ans = 0; i = 0
        # while tickets[k] != 0:
        #     if i >= len(tickets):
        #         i = 0
        #     if tickets[i] > 0:
        #         tickets[i] -= 1
        #         ans += 1
        #     i += 1
        # return ans

        # sol2
        ans = 0; 
        for i in range(len(tickets)):
            if i <= k:
                if tickets[i] < tickets[k]:
                    ans += tickets[i]
                else:
                    ans += tickets[k]
            else:
                if tickets[i] < tickets[k]:
                    ans += tickets[i]
                else:
                    ans += tickets[k]-1
        return ans
        
print(Solution().timeRequiredToBuy([84,49,5,24,70,77,87,8], 3))
