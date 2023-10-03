def solution(s):
    # sol1
    # ans = []
    # lst = []
    # s = s.split('{')
    # for c in s:
    #     c = c.split('{')
    #     c = c[0].split('}')
    #     c = c[0].split(',')
    #     if c != ['']: 
    #         lst.append(list(map(int, c)))
    # lst.sort(key= len)
    # for a in lst:
    #     for n in a:
    #         if n not in ans:
    #             ans.append(n)
    # return ans

    # sol2
    ans = []
    s = s.replace('}}', '').replace('},', ' ').replace('{', '').split(' ')
    s.sort(key = len)
    for c in s:
        c = list(map(int, c.replace(',', ' ').split(' ')))
        for num in c:
            if num not in ans:
                ans.append(num)
    return ans

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
