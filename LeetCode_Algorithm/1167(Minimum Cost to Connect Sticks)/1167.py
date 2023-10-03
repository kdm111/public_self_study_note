'''
LeetCode 1167 : Minimum Cost to Connect Sticks
stick 길이 배열이 남겨져 있다. 
두 스틱을 합쳐서 하나의 스틱으로 만들 수 있다. 
단 하나의 스틱을 만드는 길이는 비용이된다.

오직 하나의 스틱을 남기는 데 최소 비용으로 만들어라

# sol1
time limit exceeded

'''
# sol3 time limit exceeded
# class Heap:
#     def __init__(self, arr=[]):
#         self.arr = arr

#     def heapify(self):
#         for i in range(len(self.arr)//2+1, -1, -1):
#             self.swap(i)

#     def heappop(self) -> int:
#         if self.arr:
#             ret = self.arr.pop(0)
#             self.heapify()
#             return ret

#     def heappush(self, val):
#         self.arr.append(val)
#         idx = len(self.arr)-1; 
#         while idx >= 0:
#             parent = (idx-1) // 2
#             if parent >= 0 and self.arr[parent] > self.arr[idx]:
#                 self.arr[parent], self.arr[idx] = self.arr[idx], self.arr[parent]
#                 idx = parent
#             else:
#                 break 

#     def swap(self, idx):
#         left = 2*idx+1
#         right = 2*idx+2
#         min_idx = idx
#         if left < len(self.arr) and self.arr[left] < self.arr[idx]:
#             idx = left
#         if right < len(self.arr) and self.arr[right] < self.arr[idx]:
#             idx = right
#         if idx != min_idx:
#             self.arr[idx], self.arr[min_idx] = self.arr[min_idx], self.arr[idx]
#             self.swap(min_idx)


class Heap:
    def __init__(self):
        self.arr = []
    def heapify(self, idx):
        min_idx = idx; left = 2*idx+1; right = 2*idx+2
        if left < len(self.arr) and self.arr[idx] > self.arr[left]:
            idx = left
        if right < len(self.arr) and self.arr[idx] > self.arr[right]:
            idx = right
        if min_idx != idx:
            self.arr[min_idx] , self.arr[idx] = self.arr[idx], self.arr[min_idx]
            self.heapify(min_idx)
    def heappush(self, val):
        self.arr.append(val)
        idx = len(self.arr)-1
        while idx >= 0:
            parent = (idx-1)//2
            if parent >= 0 and self.arr[parent] > self.arr[idx]:
                self.arr[parent], self.arr[idx] = self.arr[idx], self.arr[parent]
                idx = parent
            else:
                break
    def heappop(self) -> int:
        if self.arr:
            ret = self.arr.pop(0)
            for i in range(len(self.arr)//2, -1, -1):
                self.heapify(i)
            return ret
class Solution:
    def connectSticks(self, sticks: list[int]) -> int:
        # sol1 333ms 63% 15MB 74%
        # import heapq
        # heapq.heapify(sticks)
        # ans = 0
        # while len(sticks) > 1:
        #     cost = heapq.heappop(sticks) + heapq.heappop(sticks)
        #     heapq.heappush(sticks, cost)
        #     ans += cost
        #     print(ans)
        # return ans

        # sol2 time limit exceeded
        # ans = 0
        # while len(sticks) > 1:
        #     cost1= min(sticks); sticks.remove(min(sticks))
        #     cost2 = min(sticks); sticks.remove(min(sticks))
        #     ans += (cost1+cost2)
        #     sticks.append(cost1+cost2)
        # return ans

        # sol3
        # heap = Heap()
        # for stick in sticks:
        #     heap.heappush(stick)
        # ans = 0
        # while len(heap.arr) > 1:
        #     print(heap.arr)
        #     cost = heap.heappop()+heap.heappop()
        #     ans += cost
        #     heap.heappush(cost)
        # return ans

        # sol4
        import heapq
        heapq.heapify(sticks)
        ans = 0
        while len(sticks) > 1:
            stick1 = heapq.heappop(sticks)
            stick2 = heapq.heappop(sticks)
            ans += stick1 + stick2
            heapq.heappush(sticks, stick1+stick2)
        
        return ans
        
        
        
# [0, 3640, 6899, 10253, 14569, 19167, 24071, 30393, 38473, 47482]
# [0, 3640, 6613, 7956, 9502, 12935, 16036, 18511, 28971, 47482]
# [474, 3166, 3259, 3354, 4316, 4598, 4904, 6322, 8080, 9009]
# [474, 3166, 3354, 3259, 4598, 4316, 4904, 6322, 8080, 9009]
# print(Solution().connectSticks([1,8,3,5])) 
# print(Solution().connectSticks([2,4,3])) 

# [474, 4316, 3166, 4904, 4598, 3354, 3259, 6322, 8080, 9009]

'''
3640
10253
18209
27711
40646
56682
75193
104164
151646
151646

3640
11310
19167
30393
41703
57640
77875
105122
152604
152604
'''
print(Solution().connectSticks([3354,4316,3259,4904,4598,474,3166,6322,8080,9009])) 
# print(Solution().connectSticks([1,8,3,5])) 

