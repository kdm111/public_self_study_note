class Solution:
    def compress(self, chars: list[str]) -> int:
        # sol1 72ms 17% 14MB 25%
        j = 0; cntString = []
        while j < len(chars):
            i = j; string = ""
            while j < len(chars) and chars[i] == chars[j]:
                string += chars[j]
                j += 1
            cntString.append(string)
        while chars:
            chars.pop()
        for string in cntString:
            chars.append(string[0])
            if len(string) != 1:
                lenString = str(len(string))
                for c in lenString:
                    chars.append(c)
        return len(chars)
print(Solution().compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))
print(Solution().compress(["b","b","b","b","b","b","b","b","b","b"]))


                    