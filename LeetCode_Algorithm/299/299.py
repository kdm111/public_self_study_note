from itertools import count
import queue


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # 46ms 85%
        bull, cow = 0, 0;
        s_arr = [0] * 10
        g_arr = [0] * 10
        for s, g in zip(secret, guess):
            if s == g:
                bull += 1
            else:
                s_arr[int(s)] += 1
                g_arr[int(g)] += 1
        for i in range(10):
            cow += min(s_arr[i], g_arr[i])
        return f"{bull}A{cow}B"


#print(Solution().getHint("1807", "7810"))
#print(Solution().getHint("1123", "0111"))
print(Solution().getHint("1122", "1222"))
# 1122
# 1222
