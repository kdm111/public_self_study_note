'''
LeetCode 1332 : removePalindromeSub

'a'와 'b'로만 구성된 문자열이 존재할 때 
한 단계로 같은 문자 쌍이 제거 가능하고 
같은 문자가 아닐 경우 한 단계로 하나의 문자만 제거가능 하다
문자열을 비우는 최소 단계수는?

sol1 50ms 61% 13.9MB 53%
O(n) O(n)
a로만 이뤄진 문자열은 하나의 회문이고 b로만 이뤄진 문자열은 하나의 회문이다.
문자가 a와 b로만 이뤄져 있으므로 어떤 문자 구성이 오더라도 최대값은 2이다.
 
aaab -> aaa -> a -> ''이므로 2이고
aaa -> a -> '' 이므로 1이고
'' 0이다.

회문임을 검사하는 코드만 작성하면 문제가 해결된다.

sol2 32ms 85% 13.9MB 53%
O(n) O(1)
'''
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        # sol1
        # return 2 - (s == s[::-1]) - (s == '')

        # sol2
        if s == "":
            return (0);
        def is_palindrome(s):
            left, right = 0, len(s)-1
            while left < right:
                if s[left] != s[right]:
                    return False
                left, right = left+1, right-1
            return True
        return 2 - is_palindrome(s)
            

