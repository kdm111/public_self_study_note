class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # sol1 949ms 6%
        # if numRows == 1:
        #     return s
        # c = 0
        # num = len(s)
        # while 0 < num:
        #     if numRows <= num:
        #         num -= numRows; c += 1
        #     else:
        #         c += 1; break
        #     k = 0
        #     while k < numRows-2 and 0 < num:
        #         c += 1; k += 1; num -= 1
        
        # board = [[None for _ in range(c)] for _ in range(numRows)]
        # i, r, c = 0, 0, 0
        # while i < len(s):
        #     if r == 0:
        #         while r < numRows and i < len(s):
        #             board[r][c] = s[i]
        #             r += 1; i += 1
        #         r -= 2; c += 1
        #     if 0 < r:
        #         while 0 < r and i < len(s):
        #             board[r][c] = s[i]
        #             r -= 1; c += 1
        #             i += 1

        # ans = ""
        # for r in range(len(board)):
        #     for c in range(len(board[0])):
        #         if board[r][c] != None:
        #             ans += board[r][c]
        # return ans


        # sol2 O(n) 58ms 88%
        if numRows == 1 or numRows > len(s): return s
        temp = [""] * numRows
        for i, char in enumerate(s):
            pos = i % (numRows * 2 - 2)
            if pos >= numRows:
                temp[(numRows * 2 - 2) - pos] += char
            else:
                temp[pos] += char
        ans = ""
        for i in range(len(temp)):
            ans += temp[i]
        return ans


        


print(Solution().convert("abcdefghi", 4))
# print(Solution().convert("abcde", 3))
# print(Solution().convert("PAYPALISHIRING", 3))
# print(Solution().convert("PAYPALISHIRING", 4))



