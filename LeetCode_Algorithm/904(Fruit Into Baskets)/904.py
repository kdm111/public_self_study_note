'''
LeetCode 904 : Fruit Into Baskets
한 줄로 이루어진 과수원에서 오른쪽으로 이동하며 과일을 두 바구니에 담는다.
하지만 한번에 하나만 담을 수 있으며 담을 수 없다면 거기까지 담아야 한다.

# 1071ms 44% 20.1MB 80.5%
# 해쉬맵에 저장한 뒤 3개 이상이 될 경우 과일들을 제거해 나감
'''
class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        count, i, j = {}, 0, 0
        ans = 0
        while j < len(fruits):
            count[fruits[j]] = count.get(fruits[j], 0) + 1
            while len(count) > 2:
                count[fruits[i]] -= 1
                if count[fruits[i]] == 0:
                    del count[fruits[i]]
                i += 1
            j += 1
            ans = max(ans, j-i)
        return ans
print(Solution().totalFruit([3,3,3,1,2,1,1,2,3,3,4]))           