class Solution:
    def firstBadVersion(self, n: int) -> int:
        # [1,2,3, ..n]개의 버전이 있을 때 최초의 배드 버전을 찾는 문제
        # 단 isBadVersion이라는 api는 제공 되고 있어 체크할 수 있음
        
        # sol1 O(logn), O(1) 31~48ms 85~35%
        # 최초의 배드 버전은 이전이 good이다.
        # 그러므로 현재 bad 버전이고 이전이 good인 숫자를 찾으면 된다.
        # left = 0
        # right = n
        # while True:
        #     mid = (left+right)//2
        #     if isBadVersion(mid) == False: 
        #         left = mid+1
        #     else:
        #         if isBadVersion(mid-1) == False:
        #             return mid
        #         right = mid-1
        
        # sol2 O(n) O(1) 시간초과
        for i in range(n+1):
            if isBadVersion(i):
                return i
        # sol3
        left = 0; right = n;
        while left <= right:
            mid = left + (right-left) // 2
            if isBadVersion(mid) == False:
                safe = mid; left = mid+1
            else:
                right = mid-1
        return safe+1
        pass

def isBadVersion(n):
    bad_version = 3
    return True if n >= bad_version else False
print(Solution().firstBadVersion(5))