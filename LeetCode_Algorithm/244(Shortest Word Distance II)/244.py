from locale import windows_locale


class WordDistance:
    from typing import List
    def __init__(self, wordsDict: List[str]):
        self.hashMap = {}
        for idx, word in enumerate(wordsDict):
            if word not in self.hashMap:
                self.hashMap[word] = [idx]
            else:
                self.hashMap[word].append(idx)
    def shortest(self, word1: str, word2: str) -> int:
        lst1 = self.hashMap[word1]; lst2 = self.hashMap[word2]
        self.solve(lst1, lst2)
        return self.ans
    def solve(self, lst1, lst2):
        import sys
        self.ans = sys.maxsize
        # O(n^2) 176ms 33%
        # for num1 in lst1:
        #     for num2 in lst2:
        #         if self.ans > abs(num2-num1):
        #             self.ans = abs(num2-num1)

        # O(n) 231ms 5%
        idx_1 = 0; idx_2 = 0
        while idx_1 < len(lst1) and idx_2 < len(lst2):
            self.ans = min(self.ans, abs(lst1[idx_1]-lst2[idx_2]))
            if lst1[idx_1] < lst2[idx_2]:
                idx_1 += 1
            else:
                idx_2 += 1
            

sol = WordDistance(["practice", "makes", "perfect", "coding", "makes"])
print(sol.shortest("makes", "coding"))