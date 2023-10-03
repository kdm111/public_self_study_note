from typing import List

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # sol1
        # if (rec1[0] == rec1[2] or rec1[1] == rec1[3] or \
        #     rec2[0] == rec2[2] or rec2[1] == rec2[3]):
        #     return False

        # return not (rec1[2] <= rec2[0] or
        #             rec1[3] <= rec2[1] or
        #             rec1[0] >= rec2[2] or
        #             rec1[1] >= rec2[3])

        # sol2
        # def intersect(rec1_left, rec1_right, rec2_left, rec2_right):
        #     return min(rec1_right, rec2_right) > max(rec1_left, rec2_left)
        
        # return (intersect(rec1[0], rec1[2], rec2[0], rec2[2]) and
        #         intersect(rec1[1], rec1[3], rec2[2], rec2[3]))

        # sol3 O(1), O(1) 39~49ms 62~32% 
        # 어떤 면이 겹친다고 할 때
        # 두 구간이 겹치는 순간이 존재해야 한다.
        # (left1, right1) , (left2, right2)
        # left1 < x < right1, left2 < x < right2
        # x는 두 구간에 모두 존재 해야 하므로 
        # left1 < x < right2, left2 < x < right1
        # 그리고 두 구간이 합쳐져서 면을 형성해야 한다.
        # 따라서 x끼리 구하고 y끼리 구해야 한다.
        x_intersect = (rec1[0] < rec2[2]) and (rec2[0] < rec1[2])
        y_intersect = (rec1[1] < rec2[3]) and (rec2[1] < rec1[3])
        return x_intersect and y_intersect
        


print(Solution().isRectangleOverlap([1,1,3,3], [0,0,2,2]))