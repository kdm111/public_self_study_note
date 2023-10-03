class Solution:

    # sol1 1473 5
    def checkBallBox(self, num: int):
        string = str(num)
        box_num = 0
        for chr in string:
            box_num += int(chr)
        return box_num


    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        hash_map = {}
        for num in range(lowLimit, highLimit + 1):
            if self.checkBallBox(num) not in hash_map:
                hash_map[self.checkBallBox(num)] = 1
            else:
                hash_map[self.checkBallBox(num)] += 1
        max_v = 0
        for k in hash_map:
            if hash_map[k] > max_v:
                max_v = hash_map[k]
        return max_v

print(Solution().countBalls(19, 28))