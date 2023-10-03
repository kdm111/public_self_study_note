from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # sol1 O(n), O(n) 340~492% 95~43%
        # counting array
        # cnt = [0] * (len(nums)+1)
        # for num in nums:
        #     cnt[num] += 1

        # ans = []
        # for idx in range(1, len(cnt)):
        #     if cnt[idx] == 0:
        #         ans.append(idx)
        # return ans

        # sol2 O(n), O(n) 469~573ms 50~24%
        # hashMap
        # hashMap = {}
        # for num in nums:
        #     hashMap[num] = 1

        # ans = []
        # for num in range(1, len(nums)+1):
        #     if num not in hashMap:
        #         ans.append(num)
        # return ans


        # sol3 O(n), O(1) 408~571ms 71~24%
        # space inplace modification
        # 주어진 배열은 n의 길이를 가지고 있고
        # 1~n중에서 없는 숫자를 찾아야 한다.
        # 주어진 길이와 인덱스는
        # 1~n, 0~n-1의 구간을 갖는다.
        # 발견되는 숫자에서 -1을 한 새로운 인덱스 값을 만든다.
        # 새로운 인덱스는 존재하는 숫자를 표시하기 위해 음수로 만든다.
        # 이렇게 되면 음수인 elem의 인덱스 숫자는 존재하는 것으로 알 수 있다.    
        for idx in range(len(nums)):
            new_idx = abs(nums[idx])-1

            if nums[new_idx] > 0:
                nums[new_idx] *= -1

        ans = []
        for idx in range(1, len(nums)+1):
            if nums[idx-1] > 0:
                ans.append(idx)
        return ans

print(Solution().findDisappearedNumbers([1,3,2]))