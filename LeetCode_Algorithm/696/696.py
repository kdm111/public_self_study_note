class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # sol1 O(n), O(n) 184~265ms 81~44%
        # group by character
        # 글자가 달라지는 부분 까지 글자가 나오는 숫자를 센 뒤 
        # 더 적은 값을 취함
        # counts = []
        # curr = 1
        # for idx in range(1, len(s)):
        #     if s[idx-1] != s[idx]:
        #         counts.append(curr)
        #         curr = 1
        #     else:
        #         curr += 1
        # counts.append(curr)

        # ans = 0
        # for idx in range(1, len(counts)):
        #     ans += min(counts[idx-1], counts[idx])
        # return ans

        # sol2 O(n), O(1) 144~156ms 96~93%
        # 위에서 메모리 사용량을 O(1)으로 줄인 버전
        ans = 0
        prev, curr = 0, 1
        for idx in range(1, len(s)):
            if s[idx-1] != s[idx]:
                ans += min(prev, curr)
                prev, curr = curr, 1
            else:
                curr += 1
        return ans+min(prev, curr)
        # return ans

print(Solution().countBinarySubstrings("1100"))