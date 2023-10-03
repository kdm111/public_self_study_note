class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        # sol1 time limie exceeded at 368407186
        # 숫자를 입력 받아 숫자를 재정렬 하면서
        # 이 숫자가 2의 거듭제곱이 될 지 확인
        # sol1 O(n!)permutation + O(n)checkAns 
        # 모든 순열을 확인 한 뒤 그 숫자가 2의 거듭 제곱인지 확인
        # self.sorted_num = set()
        # self.permutation(list(str(n)), '')
        # for num in self.sorted_num:
        #     if self.is_two_power(num):
        #         return True
        # return False

        # sol2 64ms 46% O(nlogn) O(1)
        # 완전 탐색을 실행하지 않고 한 번만 하는 방법은
        # 수를 정렬한 뒤 그 수가 2의 거듭 제곱의 정렬과 같은 지 확인
        num = "".join(sorted(str(n)))
        for i in range(30):
            if "".join(sorted(str(1 << i))) == num:
                return True
        return False

    def permutation(self, head, tail):
        if len(head) == 0:
            self.sorted_num.add(tail)
        else:
            for i in range(len(head)):
                self.permutation(head[:i] + head[i+1:], tail + head[i])
                

    def is_two_power(self, num):
        for i in range(30):
            if str(1 << i) == num:
                return True
        return False
            
        
print(Solution().reorderedPowerOf2(218))