class Solution:
    def totalCost(self, costs: list[int], k: int, candidates: int) -> int:
        # 687ms 76% 29.8Mb 77%
        from heapq import heappush, heappop
        
        left_idx = 0; right_idx = len(costs) - 1
        left_min_heap = []; right_min_heap = []
        while candidates > 0:
            if left_idx > right_idx:
                break
            if left_idx < right_idx: 
                heappush(left_min_heap, costs[left_idx])
                left_idx += 1
                heappush(right_min_heap, costs[right_idx])
                right_idx -= 1
            else:
                heappush(left_min_heap, costs[left_idx])
                left_idx += 1
                break
            candidates -= 1

        ans = 0
        while k > 0:
            if left_min_heap and right_min_heap:
                if left_min_heap[0] > right_min_heap[0]:
                    ans += heappop(right_min_heap)
                    if left_idx <= right_idx:
                        heappush(right_min_heap, costs[right_idx])
                        right_idx -= 1
                else:
                    ans += heappop(left_min_heap)
                    if left_idx <= right_idx:
                        heappush(left_min_heap, costs[left_idx])
                        left_idx += 1
            elif left_min_heap:
                ans += heappop(left_min_heap)
                if left_idx <= right_idx:
                    heappush(left_min_heap, costs[left_idx])
                    left_idx += 1
            else:
                ans += heappop(right_min_heap)
                if left_idx <= right_idx:
                    heappush(right_min_heap, costs[right_idx])
                    right_idx -= 1                
            k -= 1
        return ans
        
                
# print(Solution().totalCost([17,12,10,2,7,2,11,20,8], 3, 4))
# print(Solution().totalCost([1,2,4,1], 3, 3))
# print(Solution().totalCost([57,33,26,76,14,67,24,90,72,37,30], 11, 2))
# print(Solution().totalCost([31,25,72,79,74,65,84,91,18,59,27,9,81,33,17,58], 11, 2))
# print(Solution().totalCost([18,64,12,21,21,78,36,58,88,58,99,26,92,91,53,10,24,25,20,92,73,63,51,65,87,6,17,32,14,42,46,65,43,9,75], 13, 23))
print(Solution().totalCost([60,87,94,42,12,60], 5, 4))


