from typing import List
'''
LeetCode 42 : Trapping Rain Water


# sol1 246ms 20%
# dp
왼쪽과 오른쪽에서 각각 카운트해가면서 max값과 기둥의 차이를 빼서 저장한 뒤
그 값들 중 최소값을 취함

# sol2 123ms 92% 18.1MB 99%
# two pointer
물이 차는 조건은 진행하면서 지금까지의 맥스값보다 작은 값을 만나면 찬다.
큰 값을 만나면 업데이트 한다.
left, right 진행 업데이트는 더 큰 값을 찾아서 진행한다.


'''
class Solution:
    def trap(self, height: List[int]) -> int:
        # sol1 O(n), O(n) 246ms 20%
        # left_lst = [0] * len(height); left_max = height[0]
        # right_lst = [0] * len(height); right_max = height[len(height)-1]

        # idx = 0
        # while idx < len(left_lst):
        #     if left_max > height[idx]:
        #         left_lst[idx] = left_max -height[idx]
        #     elif left_max < height[idx]:
        #         left_max = height[idx]
        #     idx += 1
        # idx = len(height)-1
        # while idx >= 0:
        #     if right_max > height[idx]:
        #         right_lst[idx] = right_max-height[idx]
        #     elif right_max < height[idx]:
        #         right_max = height[idx]
        #     idx -= 1

        # ans = 0
        # for i in range(len(left_lst)):
        #     ans += min(left_lst[i], right_lst[i])
        # return ans


        # sol2 217ms 43%
        left = 0; right = len(height)-1;
        leftMax = height[left]; rightMax = height[right]; 
        ans = 0
        while left < right:
            # 현재 left의 높이가 right의 높이보다 작을 경우
            if height[left] < height[right]:
                # leftMax가 작다면 업데이트
                if leftMax < height[left]:
                    leftMax = height[left]
                # leftMax가 크다면 rightMax값이 더 크므로 반드시 물이 찬다.
                elif leftMax > height[left]:
                    ans += leftMax-height[left]
                left += 1
            # 현재 right의 높이가 더 낮다면
            else:
                # rightMax가 작다면 업데이트
                if rightMax < height[right]:
                    rightMax = height[right]
                # rightMax가 더 크다면 왼쪽에 right의 현재 값보다 큰 높이가 있으므로 반드시 물이 찬다.
                elif rightMax > height[right]:
                    ans += rightMax-height[right]
                right -= 1
        return ans
                    

                
                

        

print(Solution().trap([4,2,0,3,2,5]))
                     #[0, 0, 1, 0, 1, 2, 1, 0, 1, 2, 1, 2]
                     #[3, 2, 3, 1, 2, 3, 2, 0, 0, 1, 0, 0]

