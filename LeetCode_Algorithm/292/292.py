
class Solution:
    def canWinNim(self, n: int) -> bool:

        # sol1 O(1), O(1) 39ms 55%
        # 내가 돌을 없애야 하는 타이밍에 4개가 남아있다면 질 수 밖에 없다.
        # <=3 이면 내가 이기고
        # 4이면 내가 지고
        # 5이면 1을 가져가면 이기고
        # 6이면 2를 가져가면 이긴다.
        # 7이면 3을 가져가면 이긴다.
        # 8이면 어떤 식으로 돌을 가져가든 상대에게 4를 남겨줄 수 없다.
        # 즉 4의 배수에서 돌의 개수가 남아 있다면 나는 질 수 밖에 없다.
        # return False if n % 4 == 0 else True
        
        # dp O(n), O(n) 50ms 24%
        # 201782680 이상의 수 시간 초과
        if n >= 201782680:
            return n % 4 != 0
        result = [True] * (n+1)
        for i in range(4, n+1):
            if result[i-3] and result[i-2] and result[i-1]:
                result[i] = False
        return result[n]
        



print(Solution().canWinNim(8))