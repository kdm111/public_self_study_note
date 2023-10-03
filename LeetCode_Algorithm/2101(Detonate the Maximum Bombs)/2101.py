'''
LeetCode 2101 : Detonate the Maximum Bombs
폭탄이 존재하고 하나의 폭탄이 터질 경우 범위 내의 모든 폭탄이 터진다.

# sol1 898ms 41% 14.7MB 19%
커넥티드를 통해 모든 이어진 폭탄을 계산한 뒤

'''
class Solution:
    def maximumDetonation(self, bombs: list[list[int]]) -> int:
        self.connected = [set() for _ in range(len(bombs))]
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i != j:
                    if self.possible(bombs[i], bombs[j]):
                        self.connected[i].add(j)
        ans = 0
        for i in range(len(bombs)):
            seen = set([i])
            ans = max(ans, self.solve(i, seen))
        return ans
                    
    def solve(self, i, seen):
        ans = 1
        for b in self.connected[i]:
            if b not in seen:
                seen.add(b)
                ans += self.solve(b, seen)
        return ans

    def possible(self, bomb1, bomb2):
        [x1, y1, r1] = bomb1
        [x2, y2, _] = bomb2
        dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        return r1 >= dist

print(Solution().maximumDetonation([[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]))
print(Solution().maximumDetonation([[2,1,3],[6,1,4]]))
