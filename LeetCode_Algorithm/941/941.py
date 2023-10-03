class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        # 206ms 83% 15.4MB 18%
        i = 0
        while i < len(arr)-1 and arr[i] < arr[i+1]:
            i += 1
        if i == len(arr)-1 or i == 0:
            return False
        while i < len(arr)-1 and arr[i] > arr[i+1]:
            i += 1
        return i == len(arr)-1
