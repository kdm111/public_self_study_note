# sol2
from operator import add

class Solution:
    # def sum(self, num1: int, num2: int) -> int:
        # 63ms 7%
        # return num1+num2

    # sol2 

    # 47ms sum 메소드를 한 단어로 정의
    # 다른 모듈에서 함수를 불러와서
    # 솔루션 클래스의 함수를 복사해와 사용
    sum = add
    
print(Solution().sum(1,2))