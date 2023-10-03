from typing  import List

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        # sol1 O(n) 224~305ms 97~63%보다 빠름
        # hashMap을 만들어서 숫자의 인덱스를 리스트에 저장한다. 
        # 가장 긴 길이의 값을 가진 리스트의 인덱스 끝과 끝 길이의 차+1를 리턴한다.
        
        # hashMap = {}
        # degree = 0
        # degreeIdx = []
        # for i in range(len(nums)):

        #     if nums[i] not in hashMap:
        #         hashMap[nums[i]] = [i]
        #     else:
        #         hashMap[nums[i]].append(i)

        #     if degree < len(hashMap[nums[i]]):
        #         degree = len(hashMap[nums[i]])
        #         degreeIdx = [nums[i]]
        #     if degree == len(hashMap[nums[i]]):
        #         degreeIdx.append(nums[i])


        # ans = 100000
        # for i in degreeIdx:
        #     temp = hashMap[i][len(hashMap[i])-1]-hashMap[i][0]+1
        #     if ans > temp: ans = temp


        # return ans


        # sol2 300~386ms 64~39%
        # 해쉬맵을 3개 만들어서 계산한다.
        # left는 처음 나온 인덱스를 저장 
        # right는 마지막에 나온 인덱스를 저장
        # count는 빈도를 계산하여 저장한다.

        left, right, count = {}, {}, {}

        for idx, val in enumerate(nums):
            if val not in left: left[val] = idx
            right[val] = idx
            # .get(idx, value )
            # .get은 dict[idx]가 있을 경우 dict[idx]를 리턴하고 
            # dict[idx]가 없을 경우 dict[idx]=0을 만든다.
            count[val] = count.get(val, 0)+1 

        ans = len(nums)
        degree = max(count.values())
        
        for c in count:
            if degree == count[c]:
                if ans > right[c]-left[c]+1:
                    ans = right[c]-left[c]+1
        return ans

print(Solution().findShortestSubArray([1,2,2,3,1]))