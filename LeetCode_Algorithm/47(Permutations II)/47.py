from typing import List

'''
LeetCode 47 Permutation 2
중복을 제거한 perm 만들기
sol1 T : 140ms 41% S : 14.3MB 50%
숫자 카운트를 먼저 한 뒤 그 카운트에서 하나씩 빼가면서 
그 숫자가 1이상이라면 카운트를 줄이고 뎁스를 내려감
'''
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # sol1 
        ans = []
        from collections import Counter
        counter = Counter(nums)
        def solve(path):
            if len(path) == len(nums):
                ans.append(path)
                return 
            for k in counter:
                if counter[k] > 0:
                    counter[k] -= 1
                    solve(path + [k])
                    counter[k] += 1
        path = []
        solve(path)
        return ans
        

            

print(Solution().permuteUnique([1,1,3]))