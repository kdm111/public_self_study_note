from typing import List
import heapq
from numpy import swapaxes
# import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # sol1 O(mnlogn), O(1) 32~73ms 89~5%
        # 정렬한 뒤 계속해서 충돌을 일으키고 남은 수를 리턴
        # while len(stones) > 1:
        #     stones.sort()
        #     heavy_stone = stones.pop()
        #     light_stone = stones.pop()
        #     if heavy_stone-light_stone != 0:
        #         stones.append(heavy_stone-light_stone)
        # return stones[0] if stones  else 0

        # sol2 O(n)(힙 구성에 걸리는 시간)+O(nlogn)(최소값을 찾는 시간), O(n) 16~48ms 99.95~44%
        # heapq
        # heapq.heapify는 minHeap밖에 지원하지 않는다.
        # 따라서 모든 스톤에 -를 붙여주고 heapify를 진행한다.
        # for idx in range(len(stones)):
        #     stones[idx] *= -1
        # heapq.heapify(stones)

        # while len(stones)>1:
        #     heavy_stone = heapq.heappop(stones)
        #     light_stone = heapq.heappop(stones)
        #     if heavy_stone != light_stone:
        #         heapq.heappush(stones, heavy_stone-light_stone)
        #     # print(stones)
        # return -stones[0] if stones else 0

        # sol3 O(n), O(n) 32~56ms 89~25%
        # 카운팅 배열 사용
        # 스톤의 웨이트를 인덱스로 하는 배열을 만들고
        # 스톤의 개수를 세어나간다.
        counts = [0] * (max(stones)+1)
        for stone in stones:
            counts[stone] += 1
        
        # 스톤은 같은 무게끼리 충돌하면 부숴진다.
        # 즉 /2의 나머지값을 보면 된다.
        # 나머지가 0이라면 다음 스톤으로 넘어가고
        # 나머지가 1이라면 현재 무게에 저장한 뒤 다음 스톤과 함께 계산한다.

        # curr_weight = 0
        # for weight in range(len(counts)-1, 0, -1):
        #     if curr_weight == 0:
        #         if counts[weight] % 2 == 1:
        #             curr_weight = weight
        #             counts[weight] -= 1
        #             counts[weight] = 0
        #             continue

        #     else:
        #         while counts[weight]:

        #             counts[weight] -= 1
        #             if curr_weight-weight <= weight:
        #                 counts[curr_weight-weight] += 1
        #                 if counts[weight] % 2 ==0:
        #                     curr_weight = 0; break
        #                 else:
        #                     counts[weight] = 0
        #                     curr_weight = weight; break
                         
        #             else:
        #                 curr_weight = curr_weight-weight

        #             if curr_weight == 0:
        #                 curr_weight = weight


        # return curr_weight

        # sol3 33ms 64% 13.8MB 95%
        import heapq
        temp = [-stone for stone in stones]
        heapq.heapify(temp)
        while len(temp) > 1:
            first = abs(heapq.heappop(temp))
            second = abs(heapq.heappop(temp))
            if first != second:
                heapq.heappush(temp, -abs(first-second))
        return -temp[0] if temp else 0


            


                
                 
        

        
        
        
        


def heapify(arr:List[int]):
    for idx in range(len(arr)//2, -1,- 1):
        swap(arr=arr, rootIdx=idx)

def swap(arr:List[int], rootIdx:int):
    largeIdx = rootIdx
    leftChild = 2*rootIdx+1
    rightChild = 2*rootIdx+2

    if leftChild < len(arr) and arr[largeIdx] < arr[leftChild]:
        largeIdx = leftChild
    if rightChild < len(arr) and arr[largeIdx] < arr[rightChild]:
        largeIdx = rightChild
    if largeIdx != rootIdx:
        arr[rootIdx], arr[largeIdx] = arr[largeIdx], arr[rootIdx]
        swap(arr, largeIdx)
    
    

    
print(Solution().lastStoneWeight([9,10,1,7,3]))