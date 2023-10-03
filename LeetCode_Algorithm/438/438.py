from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # sol1 brute force time exceeded
        # ans = []
        # hashMap_p = self.makeHashMap(p)
        # for idx in range(len(s)-len(p)+1):
        #     string = s[idx:idx+len(p)]
        #     temp = self.makeHashMap(string)
        #     if self.check(hashMap_p, temp):
        #         ans.append(idx)
        # return ans

        # sol2 sorting time exceeded
        # ans = []
        # p = sorted(list(p))
        # for idx in range(len(s)-len(p)+1):
        #     string = sorted(list(s[idx:idx+len(p)]))
        #     if string == p:
        #         ans.append(idx)
        # return ans

        # sol3 Counter 사용 time exceeded
        # from collections import Counter
        # ans = []
        # p_counter = Counter(p)
        # for idx in range(len(s)-len(p)+1):
        #     if p_counter == Counter(s[idx:idx+len(p)]):
        #         ans.append(idx)
        # return ans

        # sol4 O(n^2) 304ms 35%
        # 카운팅 list 제작
        # list를 그때 그때 만들지 않고
        # idx를 바꾸어 가면서 하나씩 변경한 뒤 검사
        if len(s) < len(p): return []
        ans = []
        p_list = self.makeCountingList(p)
        s_list = self.makeCountingList(s[:len(p)])
        if self.isEqual(s_list, p_list):
            ans.append(0)
        for idx in range(len(s)-len(p)):
            s_list[ord(s[idx])-ord('a')] -= 1
            s_list[ord(s[idx+len(p)])-ord('a')] += 1
            # print(idx, s[idx], idx+len(p),s[idx+len(p)])
            if self.isEqual(s_list, p_list):
                ans.append(idx+1)
        return ans
                
        
        
    def makeHashMap(self, str):
        hashMap = {}
        for char in str:
            if char not in hashMap:
                hashMap[char] = 1
            else:
                hashMap[char] += 1
        return hashMap

    def check(self, hashMap, temp):
        for key in hashMap:
            if key not in temp or hashMap[key] != temp[key]:
                return False
        return True

    def makeCountingList(self, string):
        ret = [0] * 26 
        for s in string:
            ret[ord(s)-ord('a')] += 1
        return ret

    def isEqual(self, s_list, p_list):
        for i in range(len(s_list)):
            if s_list[i] != p_list[i]:
                return False
        return True
                    


# print(Solution().findAnagrams("cbaebabacd", "abc"))
print(Solution().findAnagrams("abab", "ab"))
