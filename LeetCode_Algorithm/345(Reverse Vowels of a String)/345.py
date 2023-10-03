class Solution:
    def reverseVowels(self, s: str) -> str:
        # sol1 189ms 11%
        # 모음만 뽑아 저장한 뒤 그 들의 순서만 바꿔줌
        # list_s = list(s)
        # vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        # arr = []
        # for i in range(len(list_s)):
        #     if list_s[i] in vowels:
        #         arr.append(i)
        # for i in range(len(arr) // 2):
        #     a, b = arr[i], arr[len(arr)-1-i]
        #     list_s[a], list_s[b] = list_s[b], list_s[a]
        # return "".join(list_s)


        # sol2 70ms 82%
        # two pointer
        list_s = list(s)
        left, right = 0, len(s)-1
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        while left < right:
            while left < len(list_s) and list_s[left] not in vowels:
                left += 1
            while right >= 0 and list_s[right] not in vowels:
                right -= 1
            if left >= right:
                break ;
            list_s[left], list_s[right] = list_s[right], list_s[left]
            left += 1
            right -= 1
        return "".join(list_s)