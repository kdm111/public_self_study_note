'''
LeetCode 1010 : Pairs of Songs With Total Durations Divisible by 60
노래의 길이가 담긴 리스트가 존재할 때 
현재 노래 길이와 다음에 있는 노래 길이의 합을 더해서 60으로 나누어 떨어지는 쌍의 개수 구하기

# sol1 time limit exceeded
O(n^2) O(1)
일단 브루트 포스

# sol2 754ms 44% 18.6MB 6%
O(n) O(n)
당연히 브루트 포스는 안된다.
해쉬맵으로 나눠서 저장해야 하는 데 
여기서 key값을 time % 60으로 한 뒤 
value를 time 리스트로 하는 해쉬맵을 만든다.

# sol3 404ms 75% 17.7MB 92%
O(n) O(n)
hashMap은 불필요하게 len()연산을 필요로 하므로
카운팅 배열을 만들면 제거가 가능하다.
'''
from typing import List
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # sol1
        # ans = 0
        # for i in range(len(time)-1):
        #     for j in range(i+1, len(time)):
        #         if (time[i] + time[j]) % 60 == 0:
        #             ans += 1
        # return ans

        # sol2
        # ans = 0
        # hashMap = {}
        # for t in time:
        #     if 0 in hashMap:
        #         ans += len(hashMap[t % 60])
        #     if 60 - (t % 60) in hashMap:
        #         ans += len(hashMap[60 - (t % 60)])
        #     if (t % 60) not in hashMap:
        #         hashMap[t % 60] = [t]
        #     else:
        #         hashMap[t % 60].append(t)
        # return ans

        # sol3 
        ans = 0; cnt = [0] * 61
        for t in time:
            if t % 60 == 0:
                ans += cnt[0]
            if cnt[60 - t % 60]:
                ans += cnt[60 - t % 60]
            cnt[t % 60] += 1 
        return ans
        
 
print(Solution().numPairsDivisibleBy60([60, 60, 60]))
            
            



