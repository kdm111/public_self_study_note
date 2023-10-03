class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        # sol1 1121ms 98% 55.3MB 80%
        if not intervals: return 0
        intervals.sort(key=lambda x : x[1])
        end = intervals[0][1]
        cnt = 1
        for i in range(1, len(intervals)):
            if intervals[i][0] >= end:
                end = intervals[i][1]
                cnt += 1
        return len(intervals) - cnt

print(Solution().eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
