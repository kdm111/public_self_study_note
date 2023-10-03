'''
LeetCode 38 : Count and say
주어진 숫자 n만큼 정해진 규칙을 반복한다.
1은 one 1이므로 11이 되고 
11은 two 1's로 21이 된다.
누적되면서 반복되어 n까지 반복한다.

# sol1 50ms 86% 13.8MB 87%
규칙을 따라가면서 하나씩 
'''
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        ans = self.countAndSay(n-1)
        temp = ""; i = 0
        while i < len(ans):
            j = i + 1
            while j < len(ans) and ans[i] == ans[j]:
                j += 1
            temp += str(j-i)
            temp += str(ans[i])
            i = j
        return temp
print(Solution().countAndSay(6))
