'''
LeetCode 2300 : Successful Pairs of Spells and Potions
주문의 강도를 나타내는 spells와 물약의 강도를 나타내는 potions가 존재한다.
주문과 물약의 곱이 success이상 이면 성공으로 판단한다.
각 주문 별로 물약을 곱했을 때 성공 횟수를 리턴하라.

# sol1 time limit exceeded
O(n^2) O(1)
완전 탐색으로 곱했을 때 성공 이상이면 카운트하여 리턴한다.

# sol2 1831ms 59% 37.3MB 33%
O(nlogn) O(n)
이진 탐색으로 포션에서 성공할 수 있는 최소 인덱스를 찾는다.
'''
class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        # sol1
        # ans = [0] * len(spells)
        # for i in range(len(spells)):
        #     for j in range(len(potions)):
        #         if spells[i] * potions[j] >= success:
        #             ans[i] += 1
        # return ans

        # sol2
        potions.sort(); potionNum = len(potions)
        ans = [0] * len(spells)
        for i in range(len(spells)):
            target = success / spells[i]
            l, r = 0, len(potions)
            while l < r:
                m = (l + r) // 2
                if potions[m] >= target:
                    r = m
                else:
                    l = m + 1
                print(l, m, r, target)
            print(l, target)
            ans[i] = potionNum - l
        return ans
    
print(Solution().successfulPairs([2,3,4], [1,1,1,1], 1))
print(Solution().successfulPairs([5,1,3], [1,2,3,4,5], 7))
# print(Solution().successfulPairs([5,1,3], [1,2,2,3,4,5], 7))




'''
2 3 4
1 1 1 1
1

'''