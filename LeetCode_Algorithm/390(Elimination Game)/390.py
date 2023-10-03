'''
LeetCode 390 : Elimination Game
숫자 n이 들어오면 다음과 같은 배열이 만들어진다. 
[1,2,...n]
왼쪽에서 시작해 짝수번째로 만나는 원소들만 남기고 
다시 오른쪽에서 시작해 짝수번째로 만나는 원소들만 남긴다.
이를 배열의 길이가 1일 때 까지만 반복하여 그 원소를 리턴하라.

# sol1 42ms 93% 13.9MB 26%
O(logn) O(1)
일단 배열의 수는 //2를 따라 지워지고 
앞글자가 변하는 경우는 n이 홀수이거나 left차례로 첫번째 인덱스가 지워지는 것 뿐이다.
한 사이클을 반복할 때마다 헤드의 움직임은 *2만큼 증가한다.
따라서 n이 1이 되기 전까지 계속해서 동작을 반복하며 문제를 해결한다.


'''

class Solution:
    def lastRemaining(self, n: int) -> int:
        head = 1; move = 1; left = True
        while n != 1:
            if left or n % 2 == 1:
                head += move
            n //= 2
            move *= 2
            left = not left
        return head
            



'''

1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
2 4 6 8 10 12 14 16 18 20 22
4 8 12 16 20
8 16
16

'''

print(Solution().lastRemaining(4))
