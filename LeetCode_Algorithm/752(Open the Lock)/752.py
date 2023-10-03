from typing import List
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # sol1 970ms 58%
        # gerneral bfs

        # O(n^2 * A^n + D)
        # n은 다이얼의 개수 A는 해당하는 알파벳의 수
        # D는 deadend의 사이즈
        from collections import deque
        queue = deque([("0000", 0)])
        self.visited = set(deadends)
        while queue:
            num, cnt = queue.popleft()
            if num in self.visited:
                continue
            self.visited.add(num)
            if num == target:
                return cnt
            for i in range(4):
                one_plus = num[:i] + self.turnOneWheel(int(num[i]), 1) + num[i+1:]
                one_minus = num[:i] + self.turnOneWheel(int(num[i]), -1) + num[i+1:]
                queue.extend([(one_plus, cnt+1), (one_minus, cnt+1)])
        return -1
    def turnOneWheel(self, num, operand):
        num += operand
        if num == 10:
            return '0'
        if num == -1:
            return '9'
        return str(num)
        

        
    
print(Solution().openLock(["0201","0101","0102","1212","2002"], "0202"))
print(Solution().openLock(["8888"], "0009"))

