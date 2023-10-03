from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # sol1 O(n) O(1) 510ms 88%
        if n == 0: return len(tasks)
        # task는 모두 알파벳 대문자로만 이루어져 있음
        lst = [0] * 26
        for task in tasks:
            lst[ord(task)-ord('A')] += 1
        lst.sort()
        # idle이 가질 수 있는 최대 횟수는 (max-1) * n
        max_v = lst.pop()
        idle_time = (max_v-1) * n
        while lst and idle_time > 0:
            # idle에서 빠지는 숫자는 사이에 들어갈 수 있는 최대의 수 혹은 남은 리스트에서 최대의 숫자 중 작은 수
            idle_time -= min(max_v-1, lst.pop())
        if idle_time < 0: idle_time = 0
        return idle_time + len(tasks)
        
        
        


print(Solution().leastInterval(["A","A","A","B","B","B"], 2))