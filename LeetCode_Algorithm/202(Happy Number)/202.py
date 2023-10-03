'''
LeetCode 202 Happy number
어떤 수가 들어올 때 자리 수의 제곱의 합이 순환 되면 happy number로 인식

sol1 T : 43ms 67% S : 13.9MB 61%
T : O(n) S : O(n)

arr 배열에 넣어놓고 값이 순환 되는지 체크한다.

sol2 T : 42ms 69% S : 13.8MB 61%
T O(logn) S : O(1)
floyd cycle detection algorithm
fast 2칸씩, slow 1칸씩
속도가 다른 두 개의 포인터가 루프에 들어간다면 
결국 같은 노드를 가리키게 된다.


'''
class Solution:
    def isHappy(self, n: int) -> bool:
        # sol1 O(n), O(n) 43~58ms 67~31%
        # arr = []
        # while True:
        #     if n not in arr:
        #         arr.append(n)
        #     else:
        #         return False

        #     total_sum = 0
        #     while n > 0:
        #         n, digit = divmod(n, 10)
        #         total_sum += digit ** 2
        #     n = total_sum

        #     if n == 1:
        #         return True

        # sol2
        slow = n 
        fast = self.getNext(slow)

        while slow != 1 and fast != 1 and slow != fast:
            slow = self.getNext(slow)
            fast = self.getNext(self.getNext(fast))

        return (slow == 1) or (fast == 1)

    def getNext(self, n):
        totalSum = 0
        while n > 0:
            n, digit = divmod(n, 10)
            totalSum += digit ** 2
        return totalSum

        

        


print(Solution().isHappy(1))