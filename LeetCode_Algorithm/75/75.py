from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # sol1 66ms 12%
        # nums.sort()

        # bubble sort O(n^2) 78ms 5%
        # for i in range(len(nums)-1):
        #     for j in range(i, len(nums)):
        #         if nums[i] > nums[j]:
        #             nums[i], nums[j] = nums[j], nums[i]

        # insertion sort O(n^2) 30ms 96%
        # for idx in range(1, len(nums)):
        #     temp = nums[idx]; point = idx-1
        #     while 0 <= point and temp < nums[point]:
        #         nums[point+1] = nums[point]
        #         point -= 1
        #     nums[point+1] = temp

        # selection sort O(n^2) 51ms 39%
        # for i in range(len(nums)-1):
        #     temp = i
        #     for j in range(i+1, len(nums)):
        #         if nums[temp] > nums[j]:
        #             temp = j
        #     if i != temp:
        #         nums[i], nums[temp] = nums[temp], nums[i]

        # merge sort O(nlogn)

        # def merge_sort(nums):            
        #     if len(nums) == 1: 
        #         return nums;

        #     mid = len(nums) // 2
        #     left = nums[:mid]
        #     right = nums[mid:]

        #     sorted_left = merge_sort(left)
        #     sorted_right = merge_sort(right)

        #     sorted_nums = []
        #     idx_left = 0; idx_right = 0

        #     while idx_left < len(sorted_left) or idx_right < len(sorted_right):
        #         if idx_left == len(sorted_left):
        #             sorted_nums.append(sorted_right[idx_right])
        #             idx_right += 1; continue

        #         if idx_right == len(sorted_right):
        #             sorted_nums.append(sorted_left[idx_left])
        #             idx_left += 1; continue
                
        #         if sorted_right[idx_right] < sorted_left[idx_left]:
        #             sorted_nums.append(sorted_right[idx_right])
        #             idx_right += 1
        #         else:
        #             sorted_nums.append(sorted_left[idx_left])
        #             idx_left += 1
        #     return sorted_nums

        # quick sort O(nlogn)
        # def quick_sort(nums):
        #     if len(nums) <= 1:
        #         return nums
        #     pivot = nums[len(nums) // 2]
        #     less_nums, equal, greter_nums = [],[],[]
        #     for num in nums:
        #         if num < pivot:
        #             less_nums.append(num)
        #         elif num == pivot:
        #             equal.append(num)
        #         else:
        #             greter_nums.append(num)
        #     return quick_sort(less_nums) + equal + quick_sort(greter_nums)
        # nums = quick_sort(nums)
        
        print(nums)

print(Solution().sortColors([2,9,2,1,1,0]))
print(Solution().sortColors([2,0,1]))

        
