'''
LeetCode 266 : Palindrome Permutation
문자열이 주어질 때 순열이 순회가 될 수 있는 지 체크하라

# sol1 29ms 92% 13.9MB 56%
O(n) O(1)
해쉬맵으로 카운트해서 홀수개를 가진 글자가 2개 이상인 경우 false

'''
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        hashMap = self.engCounter()
        for c in s:
            hashMap[c] += 1
        cnt = 0
        for k in hashMap:
            if hashMap[k] % 2:
                cnt += 1
        return cnt != 1
        pass
    def engCounter(self):
        hashMap = {}
        for i in range(97, 123):
            hashMap[chr(i)] = 0
        return hashMap
