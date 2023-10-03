'''
LeetCode 1839 : Longest Substring Of All Vowels in Order
주어진 문자열에서 a,e,i,o,u가 순서대로 나오는 가장 긴 문자열의 길이를 구하라

#sol1 2446ms 6% 20.3MB 19%
자음과 모음이 모두 섞일 경우 카운트 사용

# sol2 1152ms 32% 20% 19%
문자열에자음이 없으므로 set을 통해 출력
'''
class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        # sol1
        # left = right = ans = 0
        # m = {'a' : ('e', 'o', 'i', 'u'), 
        #     'e' :('i', 'o', 'u'), 
        #     'i' : ('o','u'), 
        #     'o' : ('u'), 
        #     'u' : ()}
        # cnt = {'a' : 0, 'e' : 0, 'i' : 0, 'o' : 0, 'u' : 0}
        # while right < len(word):
        #     if word[right] in cnt:
        #         for c in m[word[right]]:
        #             if cnt[c] > 0:
        #                 cnt = {'a' : 0, 'e' : 0, 'i' : 0, 'o' : 0, 'u' : 0}
        #                 left = right
        #                 break
        #         cnt[word[right]] += 1
        #     if self.check(cnt) > 0:
        #         ans = max(ans, right-left+1)
        #     right += 1
        # return ans

        # sol2
        left = right = ans = 0
        seen = set()
        while right < len(word):
            if right > 0 and word[right-1] > word[right]:
                seen = set()
                left = right
            seen.add(word[right])
            print(word[left:right+1])
            right += 1
            if len(seen) == 5:
                ans = max(ans, right-left)
        return ans
    def check(self, cnt):
        for v in cnt.values():
            if v <= 0:
                return False
        return True
print(Solution().longestBeautifulSubstring("aeiaaioaaaaeiiiiouuuooaauuaeiu"))
            
