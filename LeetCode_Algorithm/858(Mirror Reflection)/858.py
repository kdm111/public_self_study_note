'''
LeetCode 858 : Mirror Reflection
거울로 가득찬 방이 존재한다. 각각 서남쪽에는 수신기가 없지만 나머지 3 꼭지점에는 수신기가 존재한다.
p와 q가 주어지는 데 p는 방의 가로 길이이고 q는 레이저가 동남쪽 위에서 만나는 길이이다.
가장 먼저 만나는 수신기의 번호를 리턴하라
2 1
s 0

# sol1 32ms 90% 13.9MB 63%
p는 사각형 한 변의 길이로 정사각형이라고 가정하자.
q의 위치만으로 문제를 해결해야 한다.
일단 q는 반사되면서 2번과 1번을 오간다.
q의 값이 0이라면 바로 0에 도달한다.
q의 값이 p라면 레이저는 반사되지 않고 1번에 도달한다.
q의 값이 p의 1/2라면 레이저는 한 번 반사되어 2번에 도달한다.
q의 값이 p의 1/3이라면 레이저는 두 번 반사되어 1번에 도달한다.
하지만 여기서 하나 더 생각해야 한다.

꼭지점에 도달하지 않은 경우
반사를 알기 위해서 위로 방을 붙인 형태를 생각할 수 있다.
m * p == n * q를 생각할 수 있다.
m은 방의 갯수를 의미하고 n의 경우 반사의 횟수라고 생각할 수 있다.
n이 짝수라면 2에 도달할 수밖에 없다. 
n이 홀수라면 가능한 답은 0과 1이고 m의 개수가 짝수라면 항상 1에 도달할 수 밖에 없다.
0에 도달하면 0과 1의 위치가 겹치기 때문에 절대 짝수일 때 0에 도달할 수가 없다.
그리고 짝수 개의 방과 짝수 개의 반사 횟수는 존재할 수 없다.


'''


class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        # sol1
        if q == 0:
            return 0
        m, n = 1, 1
        while m * p != n * q:
            n += 1
            m = n * q // p
        if n % 2 == 0:
            return 2
        if m % 2 == 1:
            return 1
        return 0

        
print(Solution().mirrorReflection(3,0))
print(Solution().mirrorReflection(3,1))
