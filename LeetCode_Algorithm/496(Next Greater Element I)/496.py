from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # sol1 O(mn), O(1) 312~701ms 5%
        # brute force
        # ans = []
        # for i in nums1:
        #     temp = -1
        #     flag = False
        #     j = 0
        #     while j < len(nums2):
        #         if nums2[j] == i:
        #             flag = True
        #         if flag:
        #             if i < nums2[j]:
        #                 temp = nums2[j]
        #                 break
        #         j += 1
        #     ans.append(temp)
        # return ans

        # sol2 O(n), O(n) 44~92ms 97~27%
        # stack
        # nums2에서 스택을 쌓는다.
        # 스택을 넣어놓고 기존의 있던 값보다 큰 값이 들어오면 
        # (기존값 : 큰 값)으로 해쉬맵을 만든다.
        # stack = []
        # hashMap = {}
        # for num in nums2:
        #     if len(stack) == 0 or num < stack[-1]: 
        #         stack.append(num); continue;
        #     if stack[-1] == num:
        #         continue;
        #     while stack:
        #         if stack[-1] < num:
        #             hashMap[stack.pop()] = num
        #         else:
        #             break
        #     stack.append(num)
        # for num in stack: 
        #     hashMap[num] = -1
        # for i in range(len(nums1)):
        #     nums1[i] = hashMap[nums1[i]]
        # return nums1

        # sol3 45ms 92% 14MB 93%
        stack = []
        hashMap = {}
        for num in nums1:
            hashMap[num] = -1
        for num in nums2:
            while stack and stack[-1] < num:
                hashMap[stack.pop()] = num
            stack.append(num)
        for i in range(len(nums1)):
            nums1[i] = hashMap[nums1[i]]
        return nums1

print(Solution().nextGreaterElement([4,1,2], [1,1,4,2]))
