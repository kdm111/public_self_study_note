'''
LeetCode 859 : Buddy String
s와 goal이 있을 때 s에서 두 개의 글자를 바꾸었을 때 goal과 같다면 참을 반환하라.

# sol1 36ms 86% 14.1MB 62%
O(n) O(1)
두 문장의 길이가 다르다면 False
두 문장이 같을 때 중복되는 글자가 있다면 그 두 글자를 바꿔서 true인지 확인한다.
그리고 다른 글자를 발견했을 때 저장한 뒤 2개가 넘는지 확인하고 둘이 많는지 확인한다.

'''
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal): 
            return False
        if s == goal:
            return len(set(s)) < len(s)
        diff = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff.append([s[i], goal[i]])
            if len(diff) > 2:
                return False
        return len(diff) == 2 and diff[0] == diff[1][::1]
        

                    
        

print(Solution().buddyStrings("abac", "abad"))
