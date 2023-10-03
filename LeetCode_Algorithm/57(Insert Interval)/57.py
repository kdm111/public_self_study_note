from typing import List
'''
LeetCode 57 : Insert Interval
interval에서 새로운 인터벌을 넣을 때 기존의 인터벌에 확장하거나 새로 넣어라

# sol1
새로운 시작 점보다 작은 지점까지 인터벌을 추가한다.
new_start를 만나면 제일 끝의 값과 비교해서 새로운 값을 업데이트한다.

'''
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # sol1 O(n) O(n) 114ms 62%
        new_start, new_end = newInterval
        idx = 0
        ans = []
        while idx < len(intervals) and new_start > intervals[idx][0]:
            ans.append(intervals[idx])
            idx += 1
        if not ans or ans[-1][1] < new_start:
            ans.append(newInterval)
        else:
            ans[-1][1] = max(ans[-1][1], new_end)
        while idx < len(intervals):
            start, end = intervals[idx]
            if ans[-1][1] < start:
                ans.append(intervals[idx])
            else:
                ans[-1][1] = max(ans[-1][1], end)
            idx += 1
        return ans
            
            
        pass

print(Solution().insert([[1,3],[6,9]], [2,5]))
print(Solution().insert([[1,3],[10,12]], [4,6]))

print(Solution().insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
