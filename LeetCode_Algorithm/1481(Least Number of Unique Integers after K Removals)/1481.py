'''
LeetCode 1481 : Least Number of Unique Integers after K Removals
정수 배열 arr와 정수 k가 지워진다.
배열에서 k개의 요소를 지운 뒤 가장 적은 수의 정수 개수를 구하라

# sol1 602ms 32% 35MB 30%
O(nlogn) O(n)
숫자의 빈도 수를 세고 가장 적게 나온 문자부터 지워야 한다.
숫자의 빈도 수가 k보다 작다면 빈도수 만큼 제거 후 계속한다.

'''
class Solution:
    def findLeastNumOfUniqueInts(self, arr: list[int], k: int) -> int:
        # sol1
        import heapq
        from collections import Counter
        counter= Counter(arr)
        heap = []
        for (num, cnt) in counter.items():
            heapq.heappush(heap, (cnt, num))
        while heap:
            (cnt, num) = heapq.heappop(heap)
            if cnt <= k:
                k -= cnt
            else:
                heapq.heappush(heap, (cnt, num))
                break
        return len(set(heap))
            
            
            
print(Solution().findLeastNumOfUniqueInts([5,5,4], 1))