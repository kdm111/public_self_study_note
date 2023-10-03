'''

LeetCode 507 : Perfect Number
어떤 수가 주어졌을 때 그 수로 나뉘는 수를 더한 값이 그 수가 되면 true

# sol1 97ms 21% 13.9MB 7%
O(num^0.5) O(1)
num % a == 0일 경우 
total += a + num % a을 하게 된다.
그리고 total == 2*num인지 체크한다.
'''
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 0:
            return False
        total = 0
        for i in range(1, num+1):
            if i * i > num:
                break 
            if num % i == 0:
                total += i
                if i * i != num:
                    total += num // i
        print(total)
        return total == 2 *num

print(Solution().checkPerfectNumber(28))
                        
