'''
LeetCode 131 : Palindrome Partitioning
주어진 스트링에서 가능한 서브스트링이 회문인 모든 가짓수를 리턴하라.

# sol1 688ms 76% 28.8MB 96%
O(n*2^n) O(n*2^n)
"aab"에서 가질 수 있는 모든 서브스트링은 
a aa aab이다
이 과정에서 서브 스트링이 회문이라면 그 서브스트링만 재귀로 넘긴다.


'''
class Solution:
    def partition(self, s: str) -> list[list[str]]:
        self.ans = []
        self.solve(s, [])
        return self.ans
    def solve(self, s, temp):
        if not s:
            self.ans.append(temp[:])
        for i in range(1, len(s)+1):
            if self.isPalindrome(s[:i]):
                temp.append(s[:i])
                self.solve(s[i:], temp)
                temp.pop()
            
    def isPalindrome(self, s):
        for i in range(len(s)//2):
            if s[i] != s[len(s)-i-1]:
                return False
        return True

print(Solution().partition("aab"))