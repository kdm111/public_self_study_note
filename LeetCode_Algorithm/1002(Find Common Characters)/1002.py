from typing import List
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # sol1 110ms 31%
        # O(n) O(n)
        # c가 나타날 때마다 기존에 존재하면 추가되고 
        # 기존에 있던 값은 삭제된다.
        ans = list(words[0])
        for word in words[1:]:
            new = []
            for c in word:
                if c in ans:
                    new.append(c)
                    ans.remove(c)
            ans = new
        return ans