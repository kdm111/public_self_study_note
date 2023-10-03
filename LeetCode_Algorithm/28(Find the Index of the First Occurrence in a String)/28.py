class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # sol1 O(mn)  74ms 5%
        # for h_idx in range(len(haystack)):
        #     n_idx = 0
        #     ans = h_idx
        #     while n_idx < len(needle) and h_idx < len(haystack):
        #         if haystack[h_idx] != needle[n_idx]:
        #             break
        #         h_idx += 1; n_idx += 1
        #     if n_idx == len(needle):                
        #         return ans
        # return -1

        # sol2 kmp O(m+n) 48ms 42%
        # if len(haystack) < len(needle) or not needle: return -1

        # temp = [0] * len(needle)
        # i, j = 0, 1
        # while j < len(temp):
        #     if needle[i] == needle[j]:
        #         i += 1
        #         temp[j] = i
        #         j += 1
        #     else:
        #         if i != 0:
        #             i = temp[i-1]
        #         else:
        #             temp[j] = 0
        #             j += 1

        # h_idx, n_idx = 0, 0
        # while h_idx < len(haystack):
        #     if haystack[h_idx] == needle[n_idx]:
        #         h_idx += 1; n_idx += 1
        #     if n_idx == len(needle):
        #         return h_idx-n_idx
        #     elif h_idx < len(haystack) and haystack[h_idx] != needle[n_idx]:
        #         if n_idx != 0:
        #             n_idx = temp[n_idx-1]
        #         else:
        #             h_idx += 1
        # return -1


        # sol3 37ms 91% 16.3MB 36%
        n_len = len(needle); h_len = len(haystack)
        if n_len > h_len or not needle: return -1
        kmp = [0] * n_len
        i = 0; j = 1
        while j < n_len:
            if needle[i] == needle[j]:
                i += 1
                kmp[j] = i
            else:
                if i != 0:
                    i = kmp[i-1]
                    continue
            j += 1
        i = 0; j = 0
        while j < n_len and i < h_len:
            if haystack[i] == needle[j]:
                i += 1; j += 1
            else:
                if j != 0:
                    j = kmp[j-1]
                else:
                    i += 1
        
        return i - n_len if j == n_len else -1
            

# print(Solution().strStr("hello", "ll"))
# print(Solution().strStr("aaaaa", "bba"))
# print(Solution().strStr("aaaa", "aaaa"))
print(Solution().strStr("mississippi", "issip"))
# print(Solution().strStr("mississippi", "ababc"))
# print(Solution().strStr("mississippi", "abaabab"))




# 0123456789x
# mississippi
#     issip