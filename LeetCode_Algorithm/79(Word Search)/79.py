'''
LeetCode 79 : Word Search
주어진 m*n의 그리드에서 주어지는 단어가 존재하는지 찾아라.


# sol1 8060ms 21% 13.9MB 93%
일반 dfs를 통해 단어를 하나하나 매칭해나가면서 답을 찾는다.
T : O(m * n * 4^L) : n은 셀의 개수 L은 단어의 길이 S : O(L)

# sol2 time limit exceeded 

board = [["a","a","a","a"],["a","a","a","a"],["a","a","a","a"]]
word = "aaaaaaaaaaaaa"

그래프를 통해 depth를 줄일 수 있을 것 같다.
그리드를 돌면서 그 단어를 키로하고 밸류를 좌표로 하는 딕셔너리를 만든 뒤 순회하며 백트래킹을 사용한다.

# sol3 8454ms 17% 13.9MB 52%
더 빠른 dfs 방법을 찾아야 한다.
일단 원본을 바꾸지 말라고는 하지 않았으므로 보드에 다녀간 길을 표시하면 O(n)을 줄일 수 있다.
이 방법도 내가 원하는 수준이 아니다.

# sol4 4179 ms 73.54% 13.9 MB 52.49%
O(m*n*4^L) O(L)
일반적인 dfs의 방법은 불리하다는 것을 깨달았다.
시작부터 뻣어나가는 자리수를 최소화 하기 위해 여러가지를 고려해야 한다.
1. 단어 길이가 그리드의 면적보다 더 크면 안된다.
2. 단어 카운트의 개수는 그리드에 있는 단어 개수보다 작아야 한다.
3. word의 첫째 글자와 끝 글자의 카운터를 비교하여 더 가지수가 적은 것을 선택한다.

'''
from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # sol1
        # self.board = board; self.word = word
        # self.dr = [0, 1, 0, -1]
        # self.dc = [1, 0, -1, 0]
        # for r in range(len(board)):
        #     for c in range(len(board[0])):
        #         if board[r][c] == word[0]:
        #             self.visited = [(r,c)]
        #             if self.solve(r, c, 1):
        #                 return True
        # return False

        # sol2
    #     from collections import defaultdict
    #     self.graph= defaultdict(set)
    #     self.word = word
    #     for r in range(len(board)):
    #         for c in range(len(board[0])):
    #             self.graph[board[r][c]].add((r,c))
        
    #     for (r,c) in self.graph[word[0]]:
    #         self.visited = [(r,c)]
    #         if self.solve2(0):
    #             return True
    #     return False
    
    # def solve2(self, i):
    #     if i + 1 == len(self.word):
    #         return True

    #     for (r,c) in self.graph[self.word[i]]:
    #         for (r2, c2) in self.graph[self.word[i+1]]:
    #             if (r2, c2) not in self.visited:
    #                 diff_r, diff_c = abs(r2 - r), abs(c2 - c)
    #                 if diff_r + diff_c == 1:
    #                     self.visited.append((r2,c2))
    #                     if self.solve2(i+1):
    #                         return True
    #                     self.visited.pop()
    #     return False

        # sol3
        # if not board or not word:
        #     return False
        # def dfs(r, c , i):
        #     if i == len(word):
        #         return True
        #     if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or board[r][c] != word[i]:
        #         return False
        #     temp = board[r][c]
        #     board[r][c] = '.'
        #     ret = dfs(r+1,c, i+1) or dfs(r-1,c,i+1) or dfs(r, c+1, i+1) or dfs(r,c-1,i+1)
        #     board[r][c] = temp
        #     return ret
        # for r in range(len(board)):
        #     for c in range(len(board[0])):
        #         if dfs(r,c,0):
        #             return True
        # return False
        
        # sol4
        def exist(self, board: List[List[str]], word: str) -> bool:
            m, n = len(board), len(board[0])
            from collections import Counter
            from itertools import chain
            if len(word) > m * n: return False
            cnt = Counter(word)
            if cnt[word[0]] > cnt[word[-1]]:
                word = word[::-1]
            
            def dfs(r, c, i):
                if i == len(word):
                    return True
                if 0 <= r < m and 0 <= c < n and board[r][c] == word[i]:
                    temp = board[r][c]
                    board[r][c] = '.'
                    di = [[0,1],[1,0],[0,-1],[-1,0]]
                    ret = any(dfs(r+di[d][0], c+di[d][1], i+1) for d in range(len(di)))
                    board[r][c] = temp
                    return ret
                else:
                    return False
            return any(dfs(r, c, 0) for c in range(n) for r in range(m))
    # def solve(self, r, c, i):
    #     if i == len(self.word):
    #         return True
    #     for d in range(len(self.dr)):
    #         new_r, new_c = r + self.dr[d], c + self.dc[d]
    #         if 0 <= new_r < len(self.board) and 0 <= new_c < len(self.board[0]):
    #             if self.board[new_r][new_c] == self.word[i]:
    #                 if (new_r, new_c) not in self.visited:
    #                     self.visited.append((new_r, new_c))
    #                     if self.solve(new_r, new_c, i + 1):
    #                         return True
    #                     self.visited.pop()
    #     return False
