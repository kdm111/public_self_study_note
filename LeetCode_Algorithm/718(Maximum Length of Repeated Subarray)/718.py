'''
LeetCode 718 : Maximum Length of Repeated Subarray
두 숫자 리스트에서 겹치는 가장 긴 거리를 구하라.

# sol1 2831ms 74% 39.3MB 48%
O(n^2) O(n^2)
dp로 2d 어레이를 만든 뒤 두 단어가 같다면 [r+1][c+1]의 값에 +1을 한다.
'''
class Solution:
    def findLength(self, nums1: list[int], nums2: list[int]) -> int:
        ans = 0
        dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1)+1)]
        for idx1 in range(len(nums1)-1, -1, -1):
            for idx2 in range(len(nums2)-1, -1, -1):
                if nums1[idx1] == nums2[idx2]:
                    dp[idx1][idx2] = dp[idx1+1][idx2+1]+1
                    ans = max(dp[idx1][idx2], ans)
        return ans
        


# print(Solution().findLength([0,0,0,0,0,0,1,0,0,0], [0,0,0,0,0,0,0,1,0,0]))
print(Solution().findLength([1,2,3,2,1], [3,2,1,4,7]))

'''
  1 2 3 2 1 0
3 0 0 0     0
2       2 0 0
1 1 0 0 0 1 0
4 0 0 0 0 0 0
7 0 0 0 0 0 0
0 0 0 0 0 0 0
'''
# [5, 1, 2, 3, 4], [1, 2, 3, 4, 5]