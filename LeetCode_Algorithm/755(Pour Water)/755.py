'''
LeetCode 755 : Pour Water
정수 배열이 존재하고 이 정수 배열은 높이를 상징한다.
k에서 부터 시작해서 규칙에 따라 물을 붓는다.
물은 더 낮은 곳으로 이동하던가 같은 곳으로 이동이 가능하다.

# sol1 50ms 97% 13.9MB 87%
인덱스를 왼쪽으로 진행시키며 시작한다.
최소가 되는 지점을 찾아야 하기 때문에 이동이 가능하면 가능 시키며 진행한다.
그리고 오른쪽으로 이동하면서 최소점을 찾는다.
그리고 모든 면이 평평하다면 원래 인덱스에 물을 추가한다.

'''
class Solution:
    def pourWater(self, heights: list[int], volume: int, k: int) -> list[int]:
        length = len(heights)        
        idx = k
        while volume > 0:
            while idx > 0 and heights[idx] >= heights[idx-1]: 
                idx -= 1
            while idx < length - 1 and heights[idx] >= heights[idx+1]: 
                idx += 1                  
            while idx > k and heights[idx] == heights[idx-1]: 
                idx -= 1       
            heights[idx] += 1
            volume -= 1
        return heights
            
            
                
print(Solution().pourWater([2,1,1,2,1,2,2], 4, 3))
print(Solution().pourWater([1,2,3,4], 2, 2))
# print(Solution().pourWater([3,1,3], 5, 1))
# print(Solution().pourWater([1,2,3,4,3,2,1,2,3,4,3,2,1], 10, 2))


'''
[1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1]
0 1 2 3 4 5
[4, 4, 4, 4, 3, 3, 3, 3, 3, 4, 3, 2, 1]
'''