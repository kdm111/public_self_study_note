'''
LeetCode  455 : Assign Cookies

# sol1 175ms 67% 15.7MB 79%
O(nlogn) O(n)
정렬 후 크기가 크면 두 인덱스를 같이 증가시키고 아니라면 
쿠키의 인덱스만 증가시킨다.
'''
class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort(); s.sort()
        g_i = 0; s_i = 0; ans = 0
        while g_i < len(g) and s_i < len(s):
            if g[g_i] <= s[s_i]:
                g_i += 1; s_i += 1; 
                ans += 1;
            else:
                s_i += 1
        return ans
