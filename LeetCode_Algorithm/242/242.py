from ast import Try


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sol1 O(nlogn), O(n) 67~106ms 56~10%
        # if len(s) != len(t): return False
        # s_sort = sorted(list(s))
        # t_sort = sorted(list(t))

        # for i in range(len(s_sort)):
        #     if s_sort[i] != t_sort[i]:
        #         return False
        # return True

        # sol2 O O(n), O(1) 68~86ms 54~28%

        if len(s)!= len(t): return False
        hashMap_s = {}
        hashMap_t = {}
        for c in s:
            if c not in hashMap_s:
                hashMap_s[c] = 1 
            else:
                hashMap_s[c] += 1

        for c in t:
            if c not in hashMap_t:
                hashMap_t[c] = 1 
            else:
                hashMap_t[c] += 1       

        for k in hashMap_s:
            if k not in hashMap_t:
                return False
            if hashMap_s[k] != hashMap_t[k]:
                return False

        return True
        


                

print(Solution().isAnagram("rat", "cat"))