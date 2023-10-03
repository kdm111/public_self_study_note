from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # sol1 O(nlogn) 169ms 6%
        intervals.sort(key=lambda x:x[0])
        for i in range(len(intervals)-1):
            if intervals[i][1] > intervals[i+1][0]:
                return False
        return True



        # sol2 brute force O(n^2) time exceeded

        # def checkOverlap(interval0, interval1):
        #     if interval1[0] <= interval0[0] < interval1[1]:
        #         return False
        #     if interval0[0] <= interval1[0] < interval0[1]:
        #         return False
        #     return True

        # for i in range(len(intervals)):
        #     for j in range(i+1, len(intervals)):
        #         if checkOverlap(intervals[i], intervals[j]) == False:
        #             return False
        # return True




        pass

# print(Solution().canAttendMeetings([[0,30],[5,10],[15,20]]))
# print(Solution().canAttendMeetings([[7,14],[2,4]]))
# print(Solution().canAttendMeetings([[6,10],[13,14],[12,14]]))
# print(Solution().canAttendMeetings([[14,20],[6,14],[4,9]]))
print(Solution().canAttendMeetings([[5,8], [6,8]]))



