from typing import List

class SparseVector:
    # 2737ms 25%
    def __init__(self, nums: List[int]):
        self.lst = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        # ans = 0
        # i = 0
        # while i < len(vec.lst):
        #     ans += self.lst[i] * vec.lst[i]
        #     i += 1
        # return ans 

        ans = 0
        for num1, num2 in zip(self.lst, vec.lst):
            ans += (num1 * num2)
        return ans


# Your SparseVector object will be instantiated and called as such:
nums1 = [1,0,0,2,3]
nums2 = [0,3,0,4,0]
v1 = SparseVector(nums1)
v2 = SparseVector(nums2)
ans = v1.dotProduct(v2)
print(ans)