'''
LeetCode 1328 : Break a Palindrome
회문이 주어질 때 단 하나의 글자만 바꿔서 문장을 교체하라
문장은 문법적으로 가장 작은 글자와 교체해야 한다.
 문자열을 리턴하라.

# sol1 38ms 77% 13.8MB 62%

O(n) O(n)
회문의 절반만을 순회한다.
주어진 회문은 절대적으로 회문이므로 처음부터 0~length // 2부터 'a'인지 확인한다.
'a'라면 다음으로 넘어가고 'a'가 아니라면 'a'로 치환하고 리턴한다.
이제 절반이 모두 'a'에 해당하면 맨 마지막 글자만 'b'로 치환해 리턴한다.

'''
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        palindrome = list(palindrome)
        for i in range(len(palindrome)//2):
            if palindrome[i] != 'a':
                palindrome[i] = 'a'
                return "".join(palindrome)
        palindrome[len(palindrome)-1] = 'b'
        return "".join(palindrome)