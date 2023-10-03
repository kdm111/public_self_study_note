class Solution:
    
    def fib(self, n: int) -> int:

        # sol1 O(n), O(1) 26~50ms 96_45%보다 빠름
        # if n <= 1: return n
        # first = 0
        # second = 1
        # for i in range(2, n+1):
        #     third = first+second
        #     first = second
        #     second = third
        # return third

        # sol2 O(2^n), O(n) 838~905ms 23~29%보다 빠름
        # if n<=1: return n
        # return self.fib(n-1)+self.fib(n-2)

        # sol3
        # tabulation : bottom-up방식으로 답으로 찾아감
        # O(n), O(n) 24~36ms 98~77%보다 빠름
        # if n <= 1: return n
        # cache = [0] * (n+1)
        # cache[1] = 1
        # for i in range(2, n+1):
        #     cache[i] = cache[i-1]+cache[i-2]
        # return cache[n]

        # sol4 41~60 67~35%보다 빠름
    # cache = {0 : 0, 1: 1}
        # memoization : top-down 방식으로 답을 찾아감
        # if n in self.cache: return self.cache[n]
        # self.cache[n] = self.fib(n-1)+self.fib(n-2)
        # return self.cache[n]

        # sol5 O(logn), O(logn) 28~32ms 95~88%보다 빠름
        # matrix exponentiation
        # 행렬의 곱을 계산하면 logn으로 문제를 풀 수 있음
        # [[1, 1][1, 0]]^n = [[f(n+1), f(n)][f(n), f(n-1)]]
        # n이 2의 제곱에 가까울 때 까지  연산을 logn으로 줄일 수 있음 
        # n 1 2 4 16 
        if n <= 1: return n
        matrix = [[1,1], [1,0]]  
        self.matrix_power(matrix, n-1)
        return matrix[0][0]

    def matrix_power(self, matrix, n):
        if n <= 1: return matrix

        self.matrix_power(matrix, n//2)
        self.matrix_multiply(matrix, matrix)
        basic_matrix = [[1,1], [1,0]]  
        if n%2: 
            self.matrix_multiply(matrix, basic_matrix)
        

    def matrix_multiply(self, a, b):
        
        w = a[0][0]*b[0][0] + a[0][1]*b[1][0]
        x = a[0][0]*b[0][1] + a[0][1]*b[1][1]
        y = a[1][0]*b[0][0] + a[1][1]*b[1][0]
        z = a[1][0]*b[0][1] + a[1][1]*b[1][1]

        a[0][0] = w
        a[0][1] = x
        a[1][0] = y
        a[1][1] = z



        


        
print(Solution().fib(1000000))