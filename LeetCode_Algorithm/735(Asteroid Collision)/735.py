from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # sol1 O(n) O(n) 104ms 87% 17.5MB 84$%
        ans = []
        for asteroid in asteroids:
            while ans and asteroid < 0 < ans[-1]:
                if ans[-1] < -asteroid:
                    ans.pop(); 
                    continue
                elif ans[-1] == -asteroid:
                    ans.pop(); 
                break
            else:
                ans.append(asteroid)
        return ans
    


print(Solution().asteroidCollision([5,10,-5]))
print(Solution().asteroidCollision([5,10,-11]))
print(Solution().asteroidCollision([1,2,3]))
print(Solution().asteroidCollision([-4,2,3]))
print(Solution().asteroidCollision([-4,4]))



