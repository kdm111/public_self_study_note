from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # hashMap dfs 42ms 52%
        hashMap = {
            '2' : ['a','b','c'],
            '3' : ['d','e','f'],
            '4' : ['g','h','i'],
            '5' : ['j','k','l'],
            '6' : ['m','n','o'],
            '7' : ['p','q','r','s'],
            '8' : ['t','u','v'],
            '9' : ['w','x','y','z'],
        }
        ans = []
        def solve(digits, idx, temp):
            if idx == len(digits):
                if temp != "":
                    ans.append(temp); 
                return ;
            for char in hashMap[digits[idx]]:
                temp += char
                solve(digits, idx+1, temp)
                temp = temp[:-1]
        solve(digits, 0, "")
        return ans

print(Solution().letterCombinations(""))