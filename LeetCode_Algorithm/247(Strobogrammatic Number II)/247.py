'''
LeetCode 247 : Strobogrammatic Number II
주어진 n의 길이에 해당하는 모든 strobogrammatic 숫자 리스트로 바꿔 출력

# sol1 355ms 74% 25.6MB 95%
O(N * 5^(N/2+1)) O(N * 5^(N/2))
만들어야 하는 글자의 길이 * 해쉬맵의 개수 ^ 돌아야 하는 횟수
해쉬맵을 만든 다음 종료조건을 추가하여 dfs를 통해서 계속해서 넣음

'''
from typing import List

class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        self.hashMap = {
            '0' : '0',
            '1' : '1',
            '6' : '9',
            '8' : '8',
            '9' : '6'
        }
        if n == 1:
            return ["0", "1", "8"]
        self.string = ['0'] * n
        self.ans = []
        self.dfs(0)
        return self.ans

    def dfs(self, string_idx):
        if 2 * string_idx >= len(self.string):
            self.ans.append("".join(self.string))
            return ;
        for k in self.hashMap:
            if string_idx == 0 and k == '0':
                continue
            if string_idx == len(self.string) // 2 and (k == '6' or k == '9'):
                continue
            self.string[string_idx] = k;
            self.string[len(self.string)-1-string_idx] = self.hashMap[k]
            self.dfs(string_idx+1)

print(Solution().findStrobogrammatic(3))
            
# 2 1
# 3 2 1
# 4 2 
# 5 3 2
# 6 3
# 7 4 3
# 8 4
# 9 5
# 10 5
# 11 6
# 12 6
# 13 
# 0 1 2 3 4 5 6 7 8 9 10 11 12


