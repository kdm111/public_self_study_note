# def solution(n, m, x, y, r, c, k):
#     if abs(x - r) + abs(y - c) > k:
#         return "impossible"
#     d = [(1, 0, 'd'), (0, -1, 'l'), (0, 1, 'r'), (-1, 0, 'u')]
#     queue = [(x, y, "")]
#     while queue:
#         x, y, t = queue.pop(0)
#         if x == r and y == c and len(t) == k: 
#             return t
#         for (dx, dy, ch) in d:
#             nX, nY, nT = x + dx, y + dy, t + ch
#             if 1 <= nX <= n and 1 <= nY <= m and len(nT) <= k:
#                 queue.append((nX, nY, nT))
#     return "impossible"



def solution(n, m, x, y, r, c, k):
    ans = ""; back = ""; cnt = 0
    if x < r:
        while x != r:
            ans += 'd'
            x += 1
            cnt += 1
    if y > c:
        while y != c:
            ans += 'l'
            y -= 1
            cnt += 1
    if c > y:
        while y != c:
            back += 'r'
            y += 1
            cnt += 1
    if x > r:
        while x != r:
            back += 'u'
            x -= 1
            cnt += 1
    
    while cnt < k:
        ans += 'rl'
        cnt += 2
    return ans + back if cnt == k else "impossible"


# print(solution(3,4,2,3,3,1,5))
# print(solution(2,2,1,1,2,2,2))
# print(solution(3,3,1,2,3,3,4))
print(solution(5,5,2,3,4,3,10))
