'''
LeetCode 290 : Word Pattern
문자열이 주어지고 패턴이 주어질 때 문자열이 해당 패턴에 매칭되는 지 확인

# sol2
O(n) O(n)
해쉬맵 2개를 사용하여 word와 pattern에 각각 서로 저장한 뒤 서로 매칭 되는 지 확인

'''
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        # sol1 two_hashMap 41~45ms 50~39%

        # hashMap_char = {}
        # hashMap_word = {}
        # words = s.split(" ")
        # if len(words) != len(pattern):
        #     return False
        # for c, w in zip(pattern, words):
        #     if c not in hashMap_char:
        #         if w in hashMap_word:
        #             return False
        #         else:
        #             hashMap_char[c] = w
        #             hashMap_word[w] = c
        #     else:
        #         if hashMap_char[c] != w:
        #             return False
        # return True

        # sol2 my two hashMap 34~55ms 71~16%
        
        p_hashMap = {}
        w_hashMap = {}
        words = s.split(" ")
        if len(words) != len(pattern):
            return False
        for i in range(len(pattern)):
            if words[i] not in w_hashMap and pattern[i] not in p_hashMap:
                w_hashMap[words[i]] = pattern[i]
                p_hashMap[pattern[i]] = words[i]
            elif words[i] in w_hashMap and pattern[i] in p_hashMap:
                if w_hashMap[words[i]] == pattern[i] and p_hashMap[pattern[i]] == words[i]:
                    continue
                else:
                    return False
            else:
                return False
        return True
            
        
        
            
    
print(Solution().wordPattern('abc', 'b c a'))
                