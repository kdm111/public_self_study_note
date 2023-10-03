'''
LeetCode 881 : Boats to Save People
정수 배열의 리스트가 존재하고 한계점인 limit이 존재할 때
정수를 limit까지 담을 때 최소의 수는 얼마가 되겠는가?
단 한 보트에는 두 사람 밖에 탈 수 없다.

# sol1 454ms 84% 20.8MB 62%
O(nlogn) O(n)
가장 먼저 가장 무거운 사람 먼저 보트에 탑승한다고 가정한다.
만약 가장 가벼운 사람과 무거운 사람이 limit을 초과한다면 가장 무거운 사람 먼저 태운 뒤 넘어간다.

'''
class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()
        l = 0; r = len(people)-1; ans = 0;
        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1; r -= 1
            else:
                r -= 1
            ans += 1
        return ans
                

'''
1 2 4 5 6
5 4 2 1
'''
print(Solution().numRescueBoats([1,2,4,5], 6))
print(Solution().numRescueBoats([1,2], 3))
print(Solution().numRescueBoats([3,2,2,1], 3))
print(Solution().numRescueBoats([3,5,3,4], 5))
print(Solution().numRescueBoats([2,4], 5))
print(Solution().numRescueBoats([1,2,3,5,6], 1000))





        