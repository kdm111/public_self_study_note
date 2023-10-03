from typing import List

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # sol1 O(nlogn) O(n) 415~492ms 69~47%
        # 소팅 후 각 차이를 계산
        # 만약 차이가 더 적다면 초기화 후 계산
        # arr.sort()
        # ans, diff = [], 100090000000
        # for idx in range(len(arr)-1):
        #     if diff > arr[idx+1]-arr[idx]:
        #         diff = arr[idx+1]-arr[idx]
        #         ans = [[arr[idx], arr[idx+1]]]
        #     elif diff == arr[idx+1]-arr[idx]:
        #         ans.append([arr[idx], arr[idx+1]])
        # return ans

        # sol2  O(m+n), O(m) 685~717ms 11~8%
        # counting sort
        # 음수도 있으므로 가장 작은 수를 더해서 배열을 완성시킨다.
        min_num = min(arr)
        for idx in range(len(arr)): 
            arr[idx] += abs(min_num)

        # 카운팅 배열 생성
        counts = [0] * (max(arr)+1)
        for idx in arr:
            counts[idx] += 1


        # 카운트 배열에서 두 개의 포인터를 만들어 간격을 잰다.
        # 최소의 간격일 경우 배열을 초기화하고 다시 계산한다.
        ans = []
        idx_i, idx_j = -1, -1
        diff = 10000000000000
        for idx in range(len(counts)):
            if counts[idx] >= 1:
                idx_i, idx_j = idx_j, idx
                if idx_i >= 0 and idx_j >= 0:
                    num1 = idx_i-abs(min_num)
                    num2 = idx_j-abs(min_num)

                    if diff > num2-num1:
                        ans = [[num1, num2]]
                        diff = num2-num1

                    elif diff == num2-num1:
                        ans.append([num1, num2])
        return ans

 


print(Solution().minimumAbsDifference([3,8,-10,23,19,-4,-14,27]))