class Solution:
    def reformatNumber(self, number: str) -> str:
        # sol1 33ms 88% 13.8MB 68%
        number.replace("-", "").replace(" ", "")
        i = 0; ans = []
        while i < len(number):
            if i+4 == len(number):
                ans.append(number[i:i+2])
                i += 2
            elif i+3 <= len(number):
                ans.append(number[i:i+3])
                i += 3
            else:
                ans.append(number[i:i+2])
                i += 2
        return "-".join(ans)