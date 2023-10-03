'''
LeetCode 2000 : Reverse Prefix of Word
처음 만나는 ch까지의 문자열을 뒤집어서 반환한다.

# sol1 27ms 91% 13.9MB 9%
해당하는 인덱스를 찾아 거기까지만 뒤집는다.

'''
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx = self.chIdx(word, ch)
        if idx >= 0:
            return "".join(reversed(list(word[0:idx+1]))) + "".join(word[idx+1:])
        else:
            return word
    def chIdx(self, word, ch):
        for i in range(len(word)):
            if word[i] == ch:
                return i
        return -1

print(Solution().reversePrefix("abcd", 'z'))
    