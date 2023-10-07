'''
leet 1496 : Path Crossing
NEWS로 좌표의 이동이 주어진다.
이전에 주어졌던 좌표로 이동한다면 True를 반환하라.
1 <= path <= 10 ** 4

#sol1
33ms 87% 16.3MB 66%
x,y가 가질 수있는 최대 최소값은 
-10 ** 4 <= x, y <= 10 ** 4이다.
이 값을 해싱하기 위해서는 다른 좌표의 값에 20000의 가중치를 준다면
'''
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        # sol1
        seen = set([0]); x = y = 0
        for direction in path:
            if direction == 'N':
                y += 1
            elif direction == 'W':
                x -= 1
            elif direction == 'S':
                y -= 1
            else:
                x += 1
            if self.hashing(x,y)  in seen:
                return True
            seen.add(self.hashing(x,y))
        return False
    def hashing(self, x, y):
        return 10001 * x + y
print(Solution().isPathCrossing("NES"))