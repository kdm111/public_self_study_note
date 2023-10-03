'''
LeetCode 739 : Daily Temperatures

# sol1 1396ms 90% 30.6MB 11%
O(n) O(n)
온도를 읽으면서 일자와 온도를 스택에 저장한다. 
그리고 스택을 보며 현재 온도가 더 작으면 그 날짜의 차이를 저장해 출력한다
'''
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        ans = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and stack[-1][1] < temperatures[i]:
                [day, _] = stack.pop()
                ans[day] = i - day
            stack.append([i, temperatures[i]])
        return ans

print(Solution().dailyTemperatures([73,74,75,71,69,72,76,73]))