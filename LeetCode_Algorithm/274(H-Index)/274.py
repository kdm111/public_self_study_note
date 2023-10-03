'''
h index 구하기
정렬시켜놓고 남아 있는 논문의 개수가 현재 논문 인용 횟수보다 작거나 같으면
남아있는 논문 개수와 현재 ans 중 가장 큰 값을 저장

'''
class Solution:
    def hIndex(self, citations: list[int]) -> int:

        # sol1 51ms 75%
        # citations.sort(); n = len(citations)
        # ans = 0
        # for i in range(n):
        #     if citations[i] >= n - i:
        #         ans = max(ans, n-i)
        # return ans
    

        # sol2 56ms 46%
        n = len(citations)
        cnt = [0] * (n + 1)
        for i in range(n):
            if citations[i] > n:
                cnt[n] += 1
            else:
                cnt[citations[i]] += 1
        acc = 0
        for i in range(n, -1, -1):
            acc += cnt[i]
            if acc >= i:
                return i
        return 0


    
    
    
print(Solution().hIndex([3,0,6,1,5]))
print(Solution().hIndex([1,1,3]))

                
        