class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # sol1 time exceeded
        # 카운팅 배열
        # 카운팅 배열을 만들어서 그때 그때 나오는 문자열이 포함하는지 체크
        # if len(s) < len(t): return ""
        # t_counting = [0 for _ in range(128)]
        # for char in t:
        #     t_counting[ord(char)] += 1
        # ans = ""
        # left = 0; right = left+len(t)
        # while right <= len(s):
        #     temp = s[left:right]
        #     temp_counting = [0 for _ in range(128)]
        #     for char in temp:
        #         temp_counting[ord(char)] += 1
        #     if self.check(t_counting, temp_counting):
        #         if ans == "": 
        #             ans = temp
        #         if len(ans) > len(temp):
        #             ans = temp
                
        #         left += 1
        #     else:
        #         right += 1
        #     if len(ans) == len(t):
        #         break
        # return ans

        # sol2 120ms 80%
        # hashMap 
        # 해쉬맵을 사용하여 카운트
        t_counting = len(t)
        t_hashMap = {}
        ans = ""
        for char in t:
            t_hashMap[char] = t_hashMap.get(char, 0) + 1
        left = 0; right = 0;
        while right < len(s):
            if s[right] in t_hashMap:
                t_hashMap[s[right]] -= 1
                # 만약 글자의 카운트가 초기 값이라면 카운팅 감수
                if t_hashMap[s[right]] >= 0:
                    t_counting -= 1
            # t에 들어가는 모든 글자가 문자열에 들어감
            # 카운팅이 되었다면 while문이 깨지면서 다음 단계로 나아감
            while t_counting == 0:
                # ans가 길이가  더 길거나 없다면 대입함
                if not ans or len(ans) > len(s[left:right+1]):
                    ans = s[left:right+1]
                # s[left]가 t안에 존재하는 글자라면 카운팅을 더하고 해쉬맵을 증가시킴
                if s[left] in t_hashMap:
                    t_hashMap[s[left]] += 1
                    # 만약 초기값 이상으로 올라온다면 카운트 1증가
                    if t_hashMap[s[left]] > 0:
                        t_counting += 1
                left += 1
            right += 1
        return ans



    def check(self, t_counting, temp_counting):
        for idx in range(len(t_counting)):
            if t_counting[idx] != 0 and t_counting[idx] > temp_counting[idx]:
                return False
        return True


print(Solution().minWindow("ADOBECODEBANC", "ABC"))
print(Solution().minWindow("AAAABB", "AB"))
print(Solution().minWindow("AA", "AA"))
