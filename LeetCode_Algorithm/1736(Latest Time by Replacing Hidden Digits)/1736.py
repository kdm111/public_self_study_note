'''
LeetCode 1736 : Latest Time by Replacing Hidden Digits
?가 들어있는 시간에서 가장 늦은 시간 만들기

# sol1 29ms 95% 13.8MB 70%
O(n) O(1)
조건을 다 대입하여 문제 해결
'''
class Solution:
    def maximumTime(self, time: str) -> str:
        time = list(time)
        self.hour(time)
        self.minute(time)
        return "".join(time)
    
    def hour(self, time):
        if time[0] == '?':
            if time[1] < '4' or time[1] == '?':
                time[0] = '2'
            else:
                time[0] = '1'
        if time[1] == '?':
            if time[0] < '2':
                time[1] = '9'
            else:
                time[1] = '3'
    def minute(self, time):
        if time[3] == '?':
            time[3] = '5'
        if time[4] == '?':
            time[4] = '9'

print(Solution().maximumTime("2?:4?"))