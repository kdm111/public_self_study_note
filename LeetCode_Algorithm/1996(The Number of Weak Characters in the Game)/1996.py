'''
LeetCode 1996 : The Number of Weak Characters in the Game

# sol1 1971ms 98% 68MB 25%
O(n) O(n)
defense의 인덱스를 공격력으로 한 뒤 값을 해당 공격력에서 최대 방어력을 찾는다.
그리고 현재 공격의 인덱스의 하나 더 있는 인덱스에서 맥스값을 가져온다.
현재 공격력 다음 값에서 디펜스값이 더 작다면 참이다.


'''
class Solution:
    def numberOfWeakCharacters(self, properties: list[list[int]]) -> int:
        # sol1
        maxAttack = 0
        for [a, _] in properties:
            if maxAttack< a:
                maxAttack = a
        
        defense = [0] * (maxAttack + 2)
        
        for [a, d] in properties:
            defense[a] = max(defense[a], d)

        for i in range(maxAttack-1, -1, -1):
            defense[i] = max(defense[i], defense[i+1])
        
        ans = 0
        for [a,d] in properties:
            if d < defense[a+1]:
                ans += 1
        return ans

            
        
        

print(Solution().numberOfWeakCharacters([[2,2],[3,3]]))