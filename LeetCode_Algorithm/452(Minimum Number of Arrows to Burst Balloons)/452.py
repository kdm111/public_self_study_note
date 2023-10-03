class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        # sol1 time limit exceeded n^2
        # points.sort(key=lambda x : x[1])
        # ans = 0
        # for i in range(len(points)):
        #     if points[i] != [-1, -1]:
        #         ans += 1
        #     for j in range(i+1, len(points)):
        #         if points[i][0] <= points[j][0] <= points[i][1] \
        #             or points[j][0] <= points[i][1] <= points[j][1]:
        #             points[j] = [-1, -1]
        #         else:
        #             break
        #     points[i] = [-1, -1]
        # return ans

        # sol2 1122ms 99.95% 62.86MB 19%
        # 정렬 후 최대점이 다음 점의 최소점을 넘는지 확인한다.
        points.sort(key=lambda x : x[1])
        max_x = points[0][1]; ans = 1
        for i in range(1, len(points)):
            if max_x >= points[i][0]:
                continue
            ans += 1
            max_x = points[i][1]
        return ans
                    
print(Solution().findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))
print(Solution().findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]))
print(Solution().findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]))
print(Solution().findMinArrowShots([[1,2],[1,8],[3,5],[8,10]]))



