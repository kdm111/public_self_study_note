from collections import defaultdict
from types import MappingProxyType
from typing import List
from xml.etree.ElementInclude import default_loader

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        # sol1 O(n) O(n) 2719ms 13%
        # 두 단어들은 두 가지의 케이스로 나누어 볼 수 있음
        # 1. 두 글자가 다른 경우
        # 두 글자가 다른 경우에 해쉬맵에 넣어놓고 뒤집어서 체크한 뒤 ans += 4
        # 2. 두 글자가 같은 경우
        # 이 경우 문장의 중심에 넣으면 회문이 되기 때문에 ans += 2를 하게 된다.

        hashMap = {}; ans = 0; temp = 0
        for word in words:
            # 두 글자가 다른 경우
            if word[0] != word[1]:
                r_word = word[::-1]
                if r_word in hashMap and hashMap[r_word] > 0:
                    hashMap[r_word] -= 1; ans += 4
                elif word not in hashMap:
                    hashMap[word] = 1
                else:
                    hashMap[word] += 1
            # 두 글자가 같은 경우
            else:
                if word in hashMap and hashMap[word] > 0:
                    hashMap[word] -= 1; ans += 4; temp -= 1
                elif word not in hashMap:
                    hashMap[word] = 1; temp += 1
                else:
                    hashMap[word] += 1; temp += 1
        if temp > 0: ans += 2
        return ans

                
            
        pass

print(Solution().longestPalindrome(["lc","cl","gg"]))
