'''
LeetCode 609 : Find Duplicate File in System
파일 경로와 파일 내용이 주어질 때 중복된 파일 리스트에 담아 리턴하라
Input: paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]
Output: [["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]

# sol1 98ms 83% 21.6MB 77%
O(n+alpha) O(n) a는 문자열 파싱 시간
해쉬맵에 파일 내용을 저장한 뒤 파일 경로를 저장한다.
만약 그 길이가 2 이상이라면 ans에 담아 반환한다.
'''
class Solution:
    def findDuplicate(self, paths: list[str]) -> list[list[str]]:
        # sol1
        hashMap = {}
        for path in paths:
            path = path.split(" ")
            addr = path[0]
            for i in range(1, len(path)):
                content = path[i][path[i].find('(')+1 : path[i].find(')')]
                if content not in hashMap:
                    hashMap[content] = [addr+'/'+path[i][:path[i].find('(')]]
                else:
                    hashMap[content].append(addr+'/'+path[i][:path[i].find('(')])
        ans = []
        for k,v in hashMap.items():
            if len(v) >= 2:
                ans.append(v)
        return ans

print(Solution().findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]))