'''
LeetCode 1704 : Determine if String Halves Are Alike
주어진 문자열의 절반이 같은 모음수 를  포함하는 확인

# sol1 43ms 84% 13.9MB 77%
O(n) O(1)
딕셔너리를 사용해서 O(1)으로 찾고자 하였다.

'''
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        second_half = first_half = 0
        vowels = {
            'a' : 1, 'e' : 1, 'i' : 1, 'o' : 1, 'u' : 1,
            'A' : 1, 'E' : 1, 'I' : 1, 'O' : 1, 'U' : 1
        }
        for i in range(len(s)):
            if i >= len(s) // 2:
                second_half += s[i] in vowels
            else:
                first_half += s[i] in vowels
        return first_half == second_half
        pass
        