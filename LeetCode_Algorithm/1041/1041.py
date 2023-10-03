class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # 45ms 43%

        dr = [-1,0,1,0]
        dc = [0,1,0,-1]

        direction = 0
        r, c = 0, 0
        # 한 번 사이클을 돌고나면 순회 경우는 2가지가 존재한다.
        # 첫 번째로 사이클이 돌아서 제자리로 돌아오면 순회하는 것으로 볼 수 있다.
        # 두 번째로 방향이 북쪽이 아니면 된다.
        # 북쪽이 아니라면 반복을 무한대로 반복하면서 원래대로 돌아간다.
        for char in instructions:
            print(r,c, direction)
            if char == 'G':
                r += dr[direction]; c += dc[direction]
            elif char == 'L':
                direction = (direction + 3) % 4
            elif char == 'R':
                direction = (direction + 1) % 4
        if (r == 0 and c == 0) or (direction != 0):
            return True
        return False

print(Solution().isRobotBounded("LGR"))