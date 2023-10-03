'''
LeetCode 1071 : Greatest Common Divisor of Strings
s문장이 t문장의 합으로 구성될 수 있는 경우 t문장의 구간을 보여라

# sol1 58ms 53% 13.9Mb 26%
O(n^2) O(n)
문장이 최소 길이로 나뉘었을 때 그 길이가 원래 문장과 매치하는 지를 찾는 문제
일단 str2는 항상 길이가 작게 만든다.
그리고 str1에서 str2만큼의 길이를 추출해서 만약에 둘이 같다면 그대로 출력하고 
아니라면 최대 공약수를 찾아 나눈뒤 재귀를 돌린다.
'''
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # sol1
        if len(str1) < len(str2):
            str1, str2 = str2, str1
        if str1[:len(str2)] == str2:
            if str1 == str2:
                return str2
            return self.gcdOfStrings(str2, str1[len(str2):])
        return ""
print(Solution().gcdOfStrings("ABABAB", "ABAB"))