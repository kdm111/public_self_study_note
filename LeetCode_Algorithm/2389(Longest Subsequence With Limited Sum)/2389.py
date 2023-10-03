'''
LeetCode 2389 : Longest Subsequence With Limited Sum

# sol1 475ms 24% 14.2MB 31%
O(m * n + nlogn) O(n)
정렬 후 사전합을 구한다. 
사전 합에서 더 커지는 순간의 인덱스 값을 넣는다.

# sol2 212ms 43% 14.1MB 71%
이진 탐색을 통해 인덱스를 찾는다.


'''
class Solution:
    def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        # sol1
        # nums.sort()
        # prefix_sum = [0] * len(nums)
        # for i in range(len(nums)):
        #     prefix_sum[i] = sum(nums[0:i+1])

        # ans = []
        # for q in range(len(queries)):
        #     if queries[q] < prefix_sum[0]:
        #         ans.append(0)
        #     else:
        #         ans.append(-1)
        #         for i in range(len(prefix_sum)):
        #             if prefix_sum[i] <= queries[q]:
        #                 ans[-1] = i + 1
        #             else:
        #                 break
        # return ans

        # sol2 
        nums.sort()
        prefix_sum = [0] * len(nums)
        for i in range(len(nums)):
            prefix_sum[i] = sum(nums[0:i+1])

        ans = []
        for q in range(len(queries)):
            if queries[q] < prefix_sum[0]:
                ans.append(0)
            else:
                ans.append(-1)
                l = 0; r = len(prefix_sum) - 1
                while l <= r:
                    mid = (l + r) // 2
                    if queries[q] == prefix_sum[mid]:
                        ans[-1] = mid + 1
                        break
                    elif prefix_sum[mid] > queries[q]:
                        r = mid - 1
                    else:
                        l = mid + 1
                if l > r:
                    ans[-1] = r + 1
        return ans
'''
1 3 7 12
    10
'''
print(Solution().answerQueries([4,5,2,1], [3,10,21]))
print(Solution().answerQueries([2,3,4,5], [1]))
