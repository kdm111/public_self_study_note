class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # sol1 255ms 12% 16.5MB 16%
        # O(n^2)
        # def solve(temp, string):
        #     for i in range(0, len(string)-len(temp)+1, len(temp)):
        #         if temp != string[i:i+len(temp)]:
        #             return False
        #     return True
        
        # for i in range(1, len(s) // 2 + 1):
        #     temp = s[:i]
        #     if solve(temp, s[i:]) and len(s[i:]) % len(temp) == 0:
        #         return True
        # return False


        # sol2 O(n) 151ms 31% 16.7MB 10%
        # 이거 한 번 더 보기
        prefix = self.kmp(s)
        l = prefix[len(s) - 1]
        return l > 0 and len(s)%(len(s)-l) == 0

    def kmp(self, string):
        i = 0; j = 1; l = len(string)
        ret = [0] * l
        while i < l and j < l:
            if string[i] == string[j]:
                ret[j] = i + 1
                i += 1
                j += 1
            else:
                if i == 0:
                    ret[j] = 0
                    j += 1
                else:
                    i = ret[i-1]
        return ret


print(Solution().repeatedSubstringPattern("aabaaba"))
print(Solution().repeatedSubstringPattern("abab"))
