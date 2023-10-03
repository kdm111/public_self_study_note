'''
LeetCode 1323 : Maximum 69 Number
6과 9로만 이루어진 숫자들 중에서 최대값을 구하라

# sol1
sol1 51ms 64% 13.8MB 54%
들어올 수 있는 숫자가 1~10000까지 이므로
10000에서부터 나누어 가며 구한다.

# sol2 27ms 87% 13.7MB 93%
문자열 리스트로 바꾼 뒤 먼저 나타나는 '6'을 '9'로 치환한 뒤
문자열 -> 정수로 리턴한다.

'''
class Solution:
    def maximum69Number (self, num: int) -> int:
        # sol1
        # flag = True
        # ans = 0; div = 10 ** 3
        # while True:
        #     num, mod = int(num % div), int(num // div)
        #     if mod == 6 and flag == True:
        #         mod = 9; flag = False
        #     ans += mod
        #     if div == 1:
        #         break ;
        #     ans *= 10; div /= 10
        # return ans

        # sol2
        num_string = list(str(num))
        for i in range(len(num_string)):
            if num_string[i] == '6':
                num_string[i] = '9'
                break
        return int("".join(num_string))
    
print(Solution().maximum69Number(9969))