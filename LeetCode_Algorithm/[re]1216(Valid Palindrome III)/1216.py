'''
LeetCode 1216 Valid Palindrome III:
주어진 문장이 k개 이하의 글자를 빼면 회문이 되는 지 확인하라

# sol1 time limit exceeded
O(n * 2^k) O(n * 2^k) 완전탐색
투 포인터에서 다른 점이 발견될 때마다 분화시켜서 찾기


'''

class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        # sol1
        return self.solve1(s, 0, len(s)-1, k)

        # sol2
        
    def solve1(self, s, left, right, k):
        if k < 0:
            return False
        if left > right:
            return True
        if s[left] == s[right]:
            return self.solve1(s, left+1, right-1, k)
        else:
            return self.solve1(s, left+1, right, k-1) or self.solve1(s, left, right-1, k-1)

print(Solution().isValidPalindrome("abcdeca" , 2))