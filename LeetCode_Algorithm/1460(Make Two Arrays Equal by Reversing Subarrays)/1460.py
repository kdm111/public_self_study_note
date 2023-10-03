'''
LeetCode 1460 : Make Two Arrays Equal by Reversing Subarrays
두 배열이 있을 때 배열의 요소의 위치를 바꿔서 동일한 배열로 만들 수 있을 수 있는지 확인

# sol1 152ms 65% 14.1MB 40%
O(n) O(n)
카운터를 만들어서 해결
'''

class Solution:
    def canBeEqual(self, target: list[int], arr: list[int]) -> bool:
        if len(target) != len(arr) or (len(set(target)) != len(set(arr))):
            return False
        t_map = self.makeMap(target); a_map = self.makeMap(arr)
        print(t_map, a_map)

        for num in t_map:
            if num not in a_map:
                return False
            a_map[num] -= t_map[num]
        for key in a_map:
            if a_map[key] != 0:
                return False
        return True
            
    def makeMap(self, arr):
        hashMap = {}
        for num in arr:
            if num not in hashMap:
                hashMap[num] = 1
            else:
                hashMap[num] += 1
        return hashMap
print(Solution().canBeEqual([1,1,1,1,1], [1,1,1,1,1]))