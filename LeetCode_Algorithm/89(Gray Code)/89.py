''''
LeetCode 89 : Gray Code
n이 주어질 때 배열은 [0,...2^n-1]이 된다.
배열의 순서는 이웃한 요소들은 1비트만 달라야 한다.

# sol1 256ms 29% 24.5MB 9%
O(2^n) O(n)
0
0 1 
00 01 11 10
000 001 011 010 110 111 101 100 
규칙이 존재하는 데 0 1에서 기존 배열에서 (0 + 배열) + (1 + 배열)을 반복한다.

# sol2 138ms 53% 21.4MB 56%
그레이 코드 int -> gray code
number ^ number >> 1
'''
class Solution:
    def grayCode(self, n: int) -> list[int]:
        # sol1
        # bi = ['0','1']
        # k = 1
        # while k < n:
        #     temp = bi[:]
        #     for i in range(len(bi)):
        #         bi[i] = '0' + bi[i]
        #     for i in range(len(bi)-1, -1, -1):
        #         bi.append('1' + temp[i])
        #     k += 1
        # ans = [0] * len(bi)
        # for i in range(len(ans)):
        #     ans[i] = int(bi[i], 2)
        # return ans
        ans = []
        for i in range(2**n):
            ans.append(i ^ i >> 1)
        return ans
        

print(Solution().grayCode(3))