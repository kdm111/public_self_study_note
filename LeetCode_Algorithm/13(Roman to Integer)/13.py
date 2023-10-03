romanToIntMap = {
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000,
    'A': 4,
    'B': 9,
    'E': 40,
    'F': 90,
    'G': 400,
    'H': 900
}

class Solution:

 
    def romanToInt(self, s: str) -> int:
        # 58ms 82% 16.2MB 98%
        ans = romanToIntMap[s[-1]]
        for i in range(len(s)-2, -1, -1):
            curr = s[i]
            curr_next = s[i+1]
            if romanToIntMap[curr] < romanToIntMap[curr_next]:
                ans -= romanToIntMap[curr]
            else:
                ans += romanToIntMap[curr]

        # 경우의 수를 모두 치환하는 방법 43ms
        # s= s.replace('IV', 'A')
        # s= s.replace('IX', 'B')
        # s= s.replace('XL', 'E')
        # s= s.replace('XC', 'F')
        # s= s.replace('CD', 'G')
        # s= s.replace('CM', 'H')
        # ans = 0
        # for i in s:
        #     ans += romanToIntMap[i]



        return ans

print(Solution().romanToInt("LVIII"))

