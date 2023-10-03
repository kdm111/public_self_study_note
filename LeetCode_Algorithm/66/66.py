from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # sol1 O(n), O(n) 39~44ms 70~57%
        for i in range(len(digits)-1 ,-1, -1):
            digits[i] = digits[i]+1
            
            if digits[i] == 10:
                digits[i] = 0; 
                if i == 0:
                    return [1]+digits
            else:
                break
        return digits

print(Solution().plusOne([9,9,9]))
            
        
        