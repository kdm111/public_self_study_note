'''
LeetCode 713 : Subarray Product Less Than K
연속된 서브 배열의 곱이 k보다 작은 모든 개수를 구하라.

# sol1 time limit exceeded
O(n^2) O(n)
brute force
완전 탐색

# sol2 979ms 34% 16.5MB 65%
O(n) O(1)
sliding window
이 방법은 양수들의 어레이일 때만 작동한다.
음수가 나왔을 때 이전에 서브 배열의 합을 계산할수 없기 때문이다.
일단 양수 곱해서 1보다 작아질 수는 없으므로 케이스를 처리해준다.
또한 계속해서 곱해다가 k보다 커지면 작아질 때까지 왼쪽의 요소로 나눈다.
그리고 temp가 작아지는 구간에서 서브 배열의 합을 다 구해야 한다.
n개의 배열에서 하나의 요소가 추가되었을 때 늘어나는 서브 배열의 개수는 
(r), (r, r-1, ), (r, r-1, .. 0)이다.
그래서 전체 길이 -1개이다.
'''
class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        # sol1
        # if k == 0:
        #     return 0
        # self.ans = 0
        # for i in range(len(nums)):
        #     self.solve(nums[i+1:], nums[i], k)
        # return self.ans

        # sol2
        if k <= 1:
            return 0
        ans = left = 0
        temp = 1
        for right,v in enumerate(nums):
            temp *= v
            while temp >= k:
                temp /= nums[left]
                left += 1
            ans += right - left + 1
        return ans
            
            
    def solve(self, arr, temp, k):
        if temp < k:
            self.ans += 1; 
        if not arr:
            return ;
        if arr[0] * temp < k:
            self.solve(arr[1:], temp * arr[0], k)
        else:
            return ;
print(Solution().numSubarrayProductLessThanK([1,2,3], 7))