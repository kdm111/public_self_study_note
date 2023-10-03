'''
LeetCode 1387 : Sort Integers by The Power Value

어떤 수 다음의 순서에 따라 1까지 연산한다.
x % 2 == 0  x //= 2
x % 2 == 1 x = 3 * x + 1
x가 3이라면 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1로 7번 연산이 진행한다.
lo, hi가 존재하고 이를 연산 횟수를 통해 오름차순으로 정렬하고 k번째 요소를 구하라.

# sol1 404ms 71% 14.4MB 49%
해쉬맵에서 현재 숫자에서 1까지 가는 비용을 저장한다.
그리고 해쉬맵에 수가 존재할 경우 즉시 함수를 종료시켜 연산을 줄인다.


'''
class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        hashMap = {}; ans = []
        for num in range(lo, hi+1):
            ans.append([num, self.solve(num, hashMap)])
        ans.sort(key = lambda x : x[1])
        return ans[k-1][0]
        
    def solve(self, num, hashMap):
        if num == 1:
            return 0
        if num in hashMap:
            return hashMap[num]
        res = 0
        if num % 2 == 0:
            res = self.solve(num//2, hashMap)+1
        if num % 2 == 1:
            res = self.solve(3*num+1, hashMap)+1
        hashMap[num] = res
        return res

print(Solution().getKth(12, 15, 2))
print(Solution().getKth(7, 11, 4))
