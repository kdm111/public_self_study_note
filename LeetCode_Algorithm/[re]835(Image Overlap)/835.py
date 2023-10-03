class Solution:
    def largestOverlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        self.ans = 0
        img = [[0] * (len(img1)+2)]
        for i in range(len(img1)):
            img.append([0] + img1[i] + [0])
        img.append([0] * (len(img1)+2))
        for r in [-1, 0, 1]:
            for c in [-1, 0, 1]:
                self.solve(img, img2, r, c)
        return self.ans
    def solve(self, img, img2, r, c):
        c = 0
        for i in range(len(img2)):
            for j in range(len(img2[0])):
                if img2[i][j] == 1 and img[i-r][j-c] == 1:
                    c += 1
        self.ans = max(self.ans, c)

print(Solution().largestOverlap([[1]], [[1]]))