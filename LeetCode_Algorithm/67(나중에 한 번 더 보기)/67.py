class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # sol1 36~49ms, 84~49%
        # 2진수로 인식하여 더한 뒤 
        # 2진수로 바꿔서 출력 
        # totalSum = int(a,2) + int(b,2)
        # return "{0:b}".format(totalSum)

        # sol2  O(max(m,n)) O(max(m,n)) 43~48ms 64~52%
        # bit by bit computation
        # zfill(n) : 문자열의 길이만큼 n으로 맞춰줌
        # 하나씩 비트를 꺼내어 계산
        # 비트가 1일 때마다 1씩 carry에 더해준다.
        # 캐리는 0,1,2,3의 경우의 수를 가지면서 00, 01, 10, 11이 될 수 있다.


        # n = max(len(a), len(b))
        # a=a.zfill(n)
        # b=b.zfill(n)
        # carry = 0
        # ans = ""

        # for i in range(len(a)-1, -1, -1):
        #     if a[i] == "1":
        #         carry += 1
        #     if b[i] == "1":
        #         carry += 1
            
        #     ans += "1" if carry % 2 == 1 else "0"
        #     carry //= 2
        # if carry == 1: ans += "1"
        # return ans[::-1]


        # sol3 O(max(m,n)), O(max(m,n)) 49~76ms 49~6%
        # bit manipulation
        # 비트 조작으로 해결하기
        # 
        # length = max(len(a), len(b))
        # a = a.zfill(length)
        # b = b.zfill(length)
        # ans = ""
        # carry = 0
        # for idx in range(len(a)-1, -1, -1):
        #     num_a, num_b = int(a[idx]), int(b[idx])
        #     digitSum = num_a ^ num_b ^ carry
        #     carry = (num_a and num_b) or (num_b and carry) or (carry and num_a)
        #     ans += str(digitSum)
        # if carry == 1: ans += "1"
        # return ans[::-1]

        # sol4(sol3)
        # 파이썬스러운 풀이
        x,y = int(a,2), int(b,2)
        while y:
            ans = x ^ y
            carry = (x & y) << 1
            x, y = ans, carry
            print(x, y)

        return bin(x)[2:] # 0bxxxx 이므로 2:로 리턴

            


        
    

print(Solution().addBinary("11", "0"))