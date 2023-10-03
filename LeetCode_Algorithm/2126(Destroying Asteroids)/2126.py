'''
LeetCode 2126 : Destroying Asteroids
주어진 질량이 있고 소행성 무리가 존재한다.
질량이 소행성보다 더 크다면 질량에 소행성이 흡수된다. 소행성의 순서는 관계없다.
모든 소행성과 충돌이 가능하다면 참, 아니라면 거짓을 반환하라.

# sol1 1323ms 17.5% 25.4MB 89%
O(nlogn) O(n)
heap을 사용한 풀이

# sol2 1092ms 82% 27.9MB 37%
정렬을 사용한 풀이
'''
class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: list[int]) -> bool:
        # sol1
        # import heapq
        # heapq.heapify(asteroids)
        # while asteroids:
        #     planet = heapq.heappop(asteroids)
        #     if mass < planet:
        #         return False
        #     mass += planet
        # return True

        # sol2
        asteroids.sort()
        for asteroid in asteroids:
            if mass < asteroid:
                return False
            mass += asteroid
        return True
    
print(Solution().asteroidsDestroyed(84, [156,197,192,14,97,160,14,5]))