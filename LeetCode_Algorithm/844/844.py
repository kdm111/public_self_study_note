from distutils.command.build import build
from turtle import back


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # sol1 O(m+n), O(m+n) 39~47ms 65~42% 
        # def backspace(s):
        #     edited = []
        #     for chr in s:
        #         if chr == "#" and len(edited) > 0:
        #             edited.pop()
        #         elif chr != "#":
        #             edited.append(chr)
        
        #         if chr != "#":
        #             edited.append(chr)
        #         elif edited:
        #            edited.pop()
        #     return edited
        # return backspace(s) == backspace(t)

        # sol2 O(m+n), O(1) 41~56ms 60~20%
        s_idx = len(s)-1; t_idx = len(t)-1

        while 0 <= s_idx or 0 <= t_idx:
            s_cnt = 0; t_cnt = 0
            while 0 <= s_idx:
                if s[s_idx] != "#" and s_cnt ==0:
                    break
                elif s[s_idx] == "#":
                    s_cnt += 1; s_idx -= 1
                elif s[s_idx] != "#":
                    s_cnt -= 1; s_idx -= 1

            while 0 <= t_idx:
                if t[t_idx] != "#" and t_cnt ==0:
                    break
                elif t[t_idx] == "#":
                    t_cnt += 1; t_idx -= 1
                elif t[t_idx] != "#":
                    t_cnt -= 1; t_idx -= 1

            if 0 <= s_idx and 0 <= t_idx:
                if s[s_idx] != t[t_idx]: return False
            s_idx -= 1; t_idx -= 1;
            
        return s_idx == t_idx
            

        # sol3 O(m+n), O(1) 34~42ms 80~57%
        # two pointer
        # s_idx = len(s)-1; t_idx = len(t)-1
        # while 0 <= s_idx or 0 <= t_idx:
        #     s_skip = 0; t_skip = 0
        #     while 0 <= s_idx:
        #         if s[s_idx] == "#":
        #             s_skip += 1; s_idx -= 1;
        #         elif 0 < s_skip:
        #             s_skip -= 1; s_idx -= 1
        #         else:
        #             break

        #     while 0 <= t_idx:
        #         if t[t_idx] == "#":
        #             t_skip += 1; t_idx -= 1;
        #         elif 0 < t_skip:
        #             t_skip -= 1; t_idx -= 1
        #         else:
        #             break
        #     if 0 <= s_idx and 0 <= t_idx:
        #         if s[s_idx] != t[t_idx]:
        #             return False
        #     s_idx -= 1; t_idx -= 1

        # return True



            

        
        
            
            




print(Solution().backspaceCompare("nzp#o#g", "b#nzp#o#g"))