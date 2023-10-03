from asyncio import format_helpers
from turtle import end_fill
from typing  import List
class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        # sol1 time limit exceeded
        # two pointer
        # idx1 = idx2 = 0;
        # ans = []
        # while idx1 < len(encoded1) and idx2 < len(encoded2):
        #     val1, _ = encoded1[idx1]; val2, _= encoded2[idx2] 
        #     val = 0; cnt = 0
        #     while 0 < encoded1[idx1][1] and 0 < encoded2[idx2][1]:
        #         val = val1 * val2
        #         cnt += 1; 
        #         encoded1[idx1][1] -= 1; 
        #         encoded2[idx2][1] -= 1;

        #     if ans and ans[-1][0] == val:
        #         ans[-1][1] += cnt
        #     else:
        #         ans.append([val, cnt])
        #     if encoded1[idx1][1] == 0: idx1 += 1
        #     if encoded2[idx2][1] == 0: idx2 += 1
        # return ans

        # sol2 4340ms 53%
        # two pointer 수정
        idx1 = idx2 = 0;
        ans = []
        while idx1 < len(encoded1) and idx2 < len(encoded2):
            val1, freq1 = encoded1[idx1]; val2, freq2= encoded2[idx2] 
            val = val1*val2; cnt = min(freq1, freq2)
            encoded1[idx1][1] -= cnt;
            encoded2[idx2][1] -= cnt;

            if ans and ans[-1][0] == val:
                ans[-1][1] += cnt
            else:
                ans.append([val, cnt])
            if encoded1[idx1][1] == 0: idx1 += 1
            if encoded2[idx2][1] == 0: idx2 += 1
        return ans

# print(Solution().findRLEArray([[1,3],[2,3]], [[6,3],[3,3]]))
# print(Solution().findRLEArray([[1,3],[2,1],[3,2]], [[2,3],[3,3]]))
print(Solution().findRLEArray([[2,2],[5,5],[1,5],[2,5],[4,2],[5,3],[1,2],[4,3],[3,2],[2,3]], [[1,1],[4,1],[3,3],[5,3],[1,4],[5,1],[4,1],[5,3],[3,5],[2,1],[1,2],[3,1],[2,1],[4,3],[3,1],[2,1]]))


