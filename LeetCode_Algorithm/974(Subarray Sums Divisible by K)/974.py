'''
LeetCode 974 : Subarray Sums Divisible by K
주어진 배열의 서브 배열의 합이 k로 나누어 떨어지는 개수를 찾아라
서브 배열은 배열에서 부분적인 연속을 말한다.

# sol1 time limit exceeded
O(n ^ 2) O(n)
배열에 각각 값을 하나씩 더해간 뒤 k로 나누어 떨어지면 +1

# sol2 301ms 94% 18.7MB 96%
O(n+k) k는 카운트 배열, n은 계속해서 더해가는 값 O(k) k개의 배열
어떤 서브 배열의 합이 k로 나누어 떨어질 경우 
sum - some = n * k
some = sum - n * k
우리는 n이 얼마인지 모르지만 각각의 요소를 k로 나눈 나머지 값을 알 수 있다.
some % k = sum % k - (n * k) % k
n * k 는 k의 배수이므로 % k는 항상 0이다.
따라서 
some % k = sum % k
some은 어떤 이전에 나올 수 있는 어떤 배열의 합이다.
즉 배열을 앞에서 부터 차례로 더해나가며 현재 total % k가 나온 횟수를 계속해서 저장해 나가야 한다.
그리고 초기에는 cntArr[0] == 1이여야 한다.


'''
class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        # sol1
        # arr = [0] * len(nums); ans = 0
        # for i in range(len(nums)):
        #     for j in range(i+1):
        #         arr[j] += nums[i]
        #         if arr[j] % k == 0:
        #             ans += 1
        # return ans

        # sol2        
        cntArr = [0] * k; cntArr[0] = 1
        total = 0; ans = 0
        for num in nums:
            total += num
            # 파이썬에서는 음수를 처리할 필요가 없다.
            ans += cntArr[total % k]
            cntArr[total % k] += 1
        print(cntArr)
        return ans

        


print(Solution().subarraysDivByK([4,5,0,-2,-3,1], 5))

'''
4 5 0 -2 -3 1
4 4 4  2  1 2
[1,1,2,0,3]

'''