class Solution:
    def simplifyPath(self, path: str) -> str:
        # sol1 77ms 5%
        # slash로 string을 나눔
        # string = []
        # i = 0
        # while i < len(path):
        #     temp = ""
        #     while i < len(path) and path[i] != '/':
        #         temp += path[i]
        #         i += 1
        #     if temp != "":
        #         string.append(temp)
        #     i += 1

        # ans = []
        # for portion in string:
        #     if portion == '..':
        #         if ans:
        #             ans.pop()
        #     elif portion == '.':
        #         continue
        #     else:
        #         ans.append(portion)
        # ans = '/'+ '/'.join(ans)
        # return ans

        # sol2 43ms 29% 14MB 33%
        string = []
        i = 0
        while i < len(path):
            temp = ""
            while i < len(path) and path[i] != '/':
                temp += path[i]
                i += 1
            if temp != "":
                string.append(temp)
            i += 1
        ans = []
        for temp in string:
            if temp == "..":
                if ans:
                    ans.pop()
            elif temp == '.':
                continue
            else:
                ans.append(temp)
        if not ans:
            return '/'
        ret = ""
        for c in ans:
            ret += '/' + c
        return ret

print(Solution().simplifyPath("...././/../home/"))
print(Solution().simplifyPath("/home/"))
print(Solution().simplifyPath("/home//foo/"))

