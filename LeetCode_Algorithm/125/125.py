from http.client import CONTINUE
from re import I


class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # sol1 n 70~110ms 49~10% 보다 빠름
        # 아스키 코드로 바꾼 뒤 공백 등등 다 지우고 체크
        # string = ""
        # for c in s:
        #     if 65 <= ord(c) <= 90:
        #         string += chr(ord(c)+32)
        #     elif 97 <= ord(c) <= 122:
        #         string += c
        #     elif 48 <= ord(c) <= 57:
        #         string += c

        # j = len(string)-1
        # i = 0
        # while i <=j:
        #     if  string[i] != string[j]:
        #         return False
        #     i += 1
        #     j -= 1
        
        # sol2 n 70~110ms 49~10% 보다 빠름
        # i = 0
        # j = len(s)-1
        # chr_i, chr_j = "", ""
        # while i <= j:
        #     if 65 <= ord(s[i]) <= 90:
        #         chr_i = chr(ord(s[i])+32)
        #     elif 97 <= ord(s[i]) <= 122:
        #         chr_i = s[i]
        #     elif 48 <= ord(s[i]) <= 57:
        #         chr_i = s[i]
        #     else:
        #         i += 1; continue
            
        #     if 65 <= ord(s[j]) <= 90:
        #         chr_j = chr(ord(s[j])+32)
        #     elif 97 <= ord(s[j]) <= 122:
        #         chr_j = s[j]
        #     elif 48 <= ord(s[j]) <= 57:
        #         chr_j = s[j]
        #     else:
        #         j -= 1; continue
            
        #     if chr_i != "" and chr_j != "":
        #         if chr_i != chr_j:
        #             return False
        #         else:
        #             i += 1
        #             j -= 1

        # return True

        # sol3 60~70ms 50~42%보다 빠름
        # isalnum() 메소드를 통해 숫자나 알파벳을 확인
        # alnum_string = filter(lambda chr : chr.isalnum(), s)
        # lowercase_string = list(map(lambda chr : chr.lower(), alnum_string))
        # reverse_string = lowercase_string[::-1]
        # for i in range(len(lowercase_string)//2):
        #     if lowercase_string[i] != reverse_string[i]:
        #         return False
        # return True

        # sol4
        left = 0
        right = len(s)-1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

        return True



print(Solution().isPalindrome(".,"))