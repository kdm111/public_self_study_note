'''

LeetCode 1235 : Check if the Sentence Is Pangram
주어진 문장이 모든 알파벳을 포함하고 있는 지 판단

# sol1 36ms 88% 13.9MB 11%
카운팅 배열을 만들어서 하나씩 제거한 뒤 카운팅 배열의 길이가 0인지 확인

# sol2 35ms 89% 13.9MB 11%
카운터를 사용해서 카운팅을 한 뒤 키를 맞춰가면서 확인

# sol3 49ms 70% 13.9MB 11%
set을 활용해서 set의 길이가 26인지 확인
'''
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # sol1
        # cnt = list(map(chr,range(97, 123)))
        # for c in sentence:
        #   if c in cnt: cnt.remove(c)
        # return len(cnt) == 0

        # sol2
        from collections import Counter
        counter = Counter(sentence)
        for c in list(map(chr, range(97, 123))):
            if counter[c] == 0:
                return False
        return True

        # sol3
        seen = set(sentence)
        return len(seen) == 26