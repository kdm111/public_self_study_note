from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        # sol1 O(n), O(1) 296~370ms 34~12%
        # for i in range(len(s)//2):
        #     s[i], s[len(s)-i-1] = s[len(s)-i-1], s[i]
        # print(s)

        # sol2 217~284ms 73~39%
        # oneline
        # s.reverse()
        # print(s)

        # sol3 208~218ms 82~73%
        # recursive
        # def swap(left, right):
        #     if left < right:
        #         s[left], s[right] = s[right], s[left]
        #         swap(left+1, right-1)
        # swap(0, len(s)-1)
        # print(s)

        # sol4
        # iterative
        left = 0; right = len(s)-1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left+1, right-1
        print(s)

print(Solution().reverseString(["h","e","l","l","o"]))
        