'''
LeetCode 823 : Binary Trees With Factors
주어진 배열에서 이진 트리를 만들되 부모 노드는 칠드런 노드의 곱과 같아야 한다.


# sol1 465ms 81% 13.9MB 99%
dp로 해결하기 위해 가장 작은 트리를 만들어가기 시작한다.
그 뒤에 부모 노드만 보고 그 위에 트리를 계속해서 붙여 나간다.
부모 노드의 왼쪽 트리와 오른쪽 트리가 존재한다면
그 왼쪽 트리가 가지고 있었던 경우의 수와 오른쪽 트리가 가지고 있었던 경우의 수를 모두 곱해 부모 트리에 더한다.

'''
class Solution:
    def numFactoredBinaryTrees(self, arr: list[int]) -> int:
        arr.sort()
        idx = set(arr)
        dp = [1] * len(arr)
        for i in range(len(arr)):
            for j in range(i):
                if arr[i] % arr[j] == 0 and arr[i] // arr[j] in idx:
                    dp[i] += dp[j] * dp[arr.index(arr[i] // arr[j])]
                    dp[i] %= (10 ** 9 + 7)
        return sum(dp) % (10 ** 9 + 7)

print(Solution().numFactoredBinaryTrees([2,4]))
print(Solution().numFactoredBinaryTrees([18,6,3,2]))

        
                    
                    
                    