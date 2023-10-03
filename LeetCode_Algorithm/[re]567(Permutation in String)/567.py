from operator import truediv


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # sol1 O(mn) time limit exceeded
        # s1 = list(s1)
        # return self.permutation(s1, s2, 0)

        # sol2 705ms 26%
        # counter 
        from collections import defaultdict
        hashMap = defaultdict(int);
        for c in s1:
            hashMap[c] += 1
        for i in range(len(s2)):
            if s2[i] in hashMap:
                hashMap[s2[i]] -= 1
            if i >= len(s1) and s2[i-len(s1)] in hashMap: 
                hashMap[s2[i-len(s1)]] += 1
            if all([hashMap[k] == 0 for k in hashMap]):
                return True
        return False
    def permutation(self, s1, s2, idx):
        if idx == len(s1):
            string = "".join(s1)
            if self.solve(string,s2):
                return True;
            return False
        for i in range(idx, len(s1)):
            s1[i], s1[idx] = s1[idx], s1[i]
            if self.permutation(s1, s2, idx+1):
                return True
            s1[i], s1[idx] = s1[idx], s1[i]
        return False

    def solve(self, pattern, string):
        p_idx, s_idx = 0, 0
        while s_idx < len(string):
            temp = s_idx
            while p_idx < len(pattern) and pattern[p_idx] == string[s_idx]:
                p_idx += 1; s_idx += 1
            if p_idx == len(pattern):
                return True
            s_idx = temp+1
            p_idx = 0
        return False
    # def kmp(self, pattern, string):
    #     # kmp algorithm
    #     pi = [0] * len(pattern)
    #     pi_idx, pattern_idx = 0, 0
    #     while pi_idx < len(pattern):
    #         if pattern[pattern_idx] == pattern[pi_idx]:
    #             pattern_idx += 1
    #             pi[pi_idx] = pattern_idx
    #             pi_idx += 1
    #         else:
                
            

    #     print(pi)
    #     s1_idx = s2_idx = 0
    #     while s2_idx < len(s2):
    #         if s1_idx == len(s1):
    #             return True
    #         if s1[s1_idx] == s2[s2_idx]:
    #             s1_idx += 1; s2_idx += 1
    #         else:
    #             if s1_idx != 0:
    #                 s1_idx = pi[s1_idx-1]
    #             else:
    #                 s2_idx += 1 
    #     return False

print(Solution().checkInclusion("ab", "eidbaooo"))
print(Solution().checkInclusion("ab", "eidboaoo"))
print(Solution().checkInclusion("prosperity","properties"))
print(Solution().checkInclusion("abc", "bbbca"))


