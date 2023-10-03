class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        # O(n) 42ms 48%
        hashMap = {
            '1' : '1',
            '6' : '9',
            '8' : '8',
            '9' : '6',
            '0' : '0'
        }
        for idx in range(len(num)//2+1):
            if num[idx] not in hashMap:
                return False
            left = hashMap[num[idx]]
            right = num[len(num)-1 - idx]
            if left != right:
                return False
        return True

print(Solution().isStrobogrammatic("2"))