'''
LeetCode 502 : IPO
회사가 IPO를 하기 전에 최대한 자본금을 모으고 싶다.
IPO 전에 할 수 있는 일은 k개 이며 현재 자본금은 w이다.
profits는 해당 일을 할 경우 얻을 수 있는 자본이고 
capital은 일을 시작하기 위해 가지고 있어야 할 자본금이다.
최대 이익을 구하라.

# sol1 1029ms 82% 36.8MB 93%
O((k+n)logn) O(n); n번의 힙푸시가 일어날 수 있고 이 과정을 k번 반복해야 한다.
현재 가지고 있는 버젯에서 가능한 가장 값이 큰 일을 찾아야 한다.
일단 여러 번 찾는 일을 막기 위해 이익과 자본금으로 이루어진 배열을 만든 뒤 자본금을 기준으로 정렬한다.
그리고 heap을 사용해 현재 가능한 일 중에서 가장 자본이 큰 일을 찾는다.
더한 뒤 k값을 줄여주면서 답을 찾는다.

'''
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        # sol1
        import heapq
        arr = []
        for i in range(len(profits)):
            arr.append([profits[i], capital[i]])
        arr.sort(key = lambda x : x[1])
        heap = []; capital_idx = 0
        while k > 0:
            while capital_idx < len(capital) and w >= arr[capital_idx][1]:
                heapq.heappush(heap, -arr[capital_idx][0])
                capital_idx += 1
            if not heap:
                break
            w += -heapq.heappop(heap)
            k -= 1
        return w

        
print(Solution().findMaximizedCapital(2, 0, [1,2,3], [0,1,1]))

'''
k = 2; w = 0
[1,2,3], [0,1,1]

[0,1,1], [1,2,3] => 0
k = 2; w = 0; [4,3,1], [0,0,3]

'''