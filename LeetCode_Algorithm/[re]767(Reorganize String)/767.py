'''
LeetCode 767 : Reorganize String
주어진 스트링에서 s의 이웃한 글자들이 같지 않도록 재정렬하라
재정렬할 수 없다면 ""을 반환하라.

# sol1 fail
해쉬맵에서 문자열의 글자 횟수를 세서 많이 나온 순으로 정렬한 뒤 문자열을 만들어 냄
s   : ogccckcwmbmxtsbmozli
my  : cmcmcmbobocgiklstwxz
ans : cocgcickmlmsmtbwbxoz
내가 볼 땐 정상인데 왜 답이 틀리게 나오는지 모르겠다.

# sol2


'''
class Solution:
    def reorganizeString(self, s: str) -> str:
        # sol1
        # if len(s) == 1:
        #     return s
        # hashMap = {}
        # for c in range(97, 123):
        #     hashMap[chr(c)] = 0
        # for c in s:
        #     hashMap[c] += 1
        
        # arr = sorted(hashMap.items(), key = lambda item : item[1], reverse=True)
        # arr = list(map(list, (a for a in arr)))
        # if arr[0][1] >= (sum(arr[1] for arr in arr) + 1) // 2:
        #     return ""
        # ans = ""; i = 0; j = 1
        # while j < 26:
        #     while arr[i][1] != 0 and arr[j][1] != 0:
        #         ans += arr[i][0]; ans += arr[j][0] 
        #         arr[i][1] -= 1; arr[j][1] -= 1
        #     arr.sort(key = lambda x : x[1], reverse=True)
        #     if arr[i][1] == 0:
        #         while i < 26 and arr[i][1] == 0:
        #             i += 1
        #     j = i + 1
        #     while j < 26 and arr[j][1] == 0:
        #         j += 1
        # if i < 26 and arr[i][1]:
        #     ans += arr[i][0]
        # return ans 

        # sol2
        import heapq

        
                

            
        

# print(Solution().reorganizeString("abbabbaaab"))
print(Solution().reorganizeString("ogccckcwmbmxtsbmozli"))
print(Solution().reorganizeString("aabbcc"))

# 0 1 2 3 4 5 6 7
'''
ogccckcwmbmxtsbmozli
cmcmcmbobocgiklstwxz
cocgcickmlmsmtbwbxoz

'b', 'b', 'c', 'c', 'c', 'c', 'g', 'i', 'k', 'l', 'm', 'm', 'm', 'o', 'o', 's', 't', 'w', 'x', 'z'
'b', 'b', 'c', 'c', 'c', 'c', 'g', 'i', 'k', 'l', 'm', 'm', 'm', 'o', 'o', 's', 't', 'w', 'x', 'z'
'''