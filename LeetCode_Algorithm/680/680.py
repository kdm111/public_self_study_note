class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        # sol1 O(n^2), O(1) 시간초과
        # brute force

        # for idx in range(len(s)):
        #     i, j = 0, len(s)-1
        #     flag = True
        #     while i < j:
        #         if i == idx: i += 1; continue;
        #         if j == idx: j -= 1; continue;

        #         if s[i] != s[j]:
        #             flag = False; break;
        #         i += 1
        #         j -= 1
        #     if flag: return True
        # return False

        # sol2 O(n), O(1) 223~326ms 36~14%
        # two pointers
        # 양쪽 끝에서 회문임을 체크할 때
        # 단어가 다른 두 포인터를 만났을 때 한 쪽을 지우고 나머지로 회문 체크를 한 뒤
        # 둘 중 하나라도 회문임이 확인 되면 True 
        i, j = 0, len(s)-1
        while i < j:

            if s[i] != s[j]:
                return self.checkPalindrome(s, i+1, j) or self.checkPalindrome(s, i, j-1)
            i += 1
            j -= 1
        return True

    def checkPalindrome(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True



                
        






print(Solution().validPalindrome("abc"))