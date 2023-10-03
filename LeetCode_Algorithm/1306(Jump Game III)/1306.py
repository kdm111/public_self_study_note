class Solution:
    def canReach(self, arr: list[int], start: int) -> bool:
        # sol1 294ms 85% 20.8MB 73%
        from collections import deque
        queue = deque([start])
        while queue:
            node = queue.popleft()
            if arr[node] == 0:
                return True
            if arr[node] > 0:
                for v in [node+arr[node], node-arr[node]]:
                    if 0 <= v < len(arr):
                        queue.append(v)
            arr[node] = -1
        return False
print(Solution().canReach([3,0,2,1,2], 2))