from typing import List
class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        
        # sol1 time limit exceeded
        # O(n^2) O(n)
        # dfs
        # 최대 레벨이 n이 될 수 있고 각 pid를 순회해야 하므로 n^2
        # self.ans = set()
        # self.dfs(pid, ppid, kill)
        # return list(self.ans)


        # sol2 1009ms 12%
        # map and dfs
        # O(n) O(n)
        # from collections import defaultdict
        # hashMap = defaultdict(set)
        # for i in range(len(ppid)):
        #     if i < len(pid):
        #         hashMap[ppid[i]].add(pid[i])
        #     else:
        #         hashMap[ppid[i]] = None
        # self.ans = set()
        # self.solve2(hashMap, kill)
        # return list(self.ans)


        # sol3 768ms 37%
        # map and queue
        # iterative
        from collections import defaultdict, deque
        hashMap = defaultdict(set)
        for i in range(len(ppid)):
            if i < len(pid):
                hashMap[ppid[i]].add(pid[i])
            else:
                hashMap[ppid[i]] = None

        ans = set()
        queue = deque([kill])
        while queue:
            node = queue.popleft()
            ans.add(node)
            queue.extend(hashMap[node])
        return list(ans)

    def dfs(self, pid, ppid, kill):
        self.ans.add(kill)
        for i in range(len(ppid)):
            if kill == ppid[i]:
                self.dfs(pid, ppid, pid[i])
    def solve2(self, map, kill):
        self.ans.add(kill)
        for child in map[kill]:
            self.solve2(map, child)

print(Solution().killProcess([1,3,10,5], [3,0,5,3], 5))
print(Solution().killProcess([1], [0], 1))
