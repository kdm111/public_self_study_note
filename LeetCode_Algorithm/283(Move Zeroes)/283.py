from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        # sol1 O(n), O(1) 210~250ms 66~48%
        # idx_num, idx_0 = 0, 0
        # while True:
        #     while idx_num < len(nums) and nums[idx_num] == 0:
        #         idx_num += 1
        #     while idx_0 < len(nums) and nums[idx_0] != 0:
        #         idx_0 += 1
        #     # print(idx_num, idx_0)
        #     if idx_num >= len(nums) or idx_0 >= len(nums):
        #         break
        #     if idx_0 > idx_num:
        #         
        #         idx_num += 1
        #         continue

        #     nums[idx_num], nums[idx_0] = nums[idx_0], nums[idx_num]

        # sol2 160~168ms 98~92%
        # temp = []
        # for num in nums:
        #     if num != 0:
        #         temp.append(num)
        # i = len(nums)-len(temp)
        # while i > 0:
        #     temp.append(0)
        #     i -= 1

        # # nums = temp[:] 
        # # nums라는 새로운 변수를 만들어서 temp의 값을 슬라이스 한다.
        # # 이 경우 기존의 nums가 아닌 새로운 변수를 만들어서 사용한 것이 된다.
        # # 따라서 기존의 nums에 복사하기 위해서는 아래의 코드를 사용해야 한다.
        # for i in range(len(temp)):
        #     nums[i] = temp[i]

        # sol3 O(n), O(1) 180~215ms 81~64%
        # 먼저 0이 나오는 인덱스를 찾는다.
        # 그리고 0과 숫자를 교환 한뒤
        # 그 다음에 0이 나오는 위치를 찾는다.
        # idx_0 = -1
        # for idx in range(len(nums)):
        #     if nums[idx] == 0:
        #         idx_0 = idx
        #         break
        # if idx_0 < 0:
        #     return
        # for idx in range(idx_0+1, len(nums)):
        #     if nums[idx] != 0:
        #         nums[idx], nums[idx_0] = nums[idx_0], nums[idx]

        #         while True:
        #             idx_0 += 1
        #             if nums[idx_0] == 0:
        #                 break
        # print(nums)


                
        # sol5 171ms 50% 17.9MB 11.9%
        # 0을 오른쪽 정렬만 시키면 된다.
        # right이 0이 아닐 때 left와 스왑이 일어난다.
        # 이때 left는 0이거나 혹은 right 자기 자신이다.
        # 자기 자신이면 스왑을 하지 않고 left가 뒤로 쳐졌다면 그것은 0이므로 스왑한다. 
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                if left != right:
                    nums[left], nums[right] = nums[right], nums[left]
                left += 1

                

                
print(Solution().moveZeroes([2,1]))