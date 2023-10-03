
'''
LeetCode 1243 : Array Transformation

# sol1 31ms 97% 13.9MB 64%
공간 복잡도를 줄이기 위해서 변수 세 개를 사용한다.
변화가 있다고 하더라도 복사한 변수에는 영향을 주지 않는다.

'''
class Solution:
    def transformArray(self, arr: list[int]) -> list[int]:
        if len(arr) < 3:
            return arr
        changed = True
        while changed:
            changed = False
            print(arr)
            prev = arr[0]; curr = arr[1]; nxt = arr[2]
            for i in range(1, len(arr)-1):
                if curr > prev and curr > nxt:
                    arr[i] -= 1; changed = True
                elif curr < prev and curr < nxt:
                    arr[i] += 1; changed = True
                if i < len(arr)-2:
                    prev = curr; curr = nxt; nxt = arr[i+2]
                else:
                    break
        return arr


print(Solution().transformArray([1,6,3,4,3,5]))