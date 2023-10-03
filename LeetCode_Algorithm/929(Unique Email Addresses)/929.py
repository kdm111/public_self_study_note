'''
LeetCode 929 : Unique Email Addresses
이메일이 리스트로 들어올 때 각각 다른 이메일의 개수 구하기
단 아이디 안에서 .나 +가 포함될 수 있다.
.는 연결 된다는 뜻이고 + 뒤에 나오는 글자들은 삭제된다.

# sol1 229ms 7% 14% 71%
# O(n) O(n)
해쉬맵으로 저장해서 카운트한다.

# sol2 91ms 71% 13.8MB 93%
# O(n) O(n)
전부다 set을 사용해서 문제를 해결한다.
'''
from typing import List
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # ans = 0
        # hashMap = {}
        # for email in emails:
        #     atSign = self.findAtSign(email)
        #     name = email[:atSign]
        #     mail = email[atSign+1:]
        #     name = self.findName(name)
        #     if mail not in hashMap:
        #         hashMap[mail] = set()
        #         hashMap[mail].add(name)
        #         ans += 1
        #     elif name not in hashMap[mail]:
        #         hashMap[mail].add(name)
        #         ans += 1
        # return ans

        # sol2
        data = set()
        for email in emails:
            atSign = self.findAtSign(email)
            name = email[:atSign]
            mail = email[atSign+1:]
            realName = self.findName(name)
            data.add(realName+'@'+mail)
        return len(data)

            
        pass
    def findAtSign(self, str):
        for i in range(len(str)):
            if str[i] == '@':
                return i
        return -1
    def findName(self, name):
        ret = ""
        for c in name:
            if c == '+':
                break 
            if c == '.':
                continue
            ret += c
        return ret
                    