# 모듈러 연산 문제

import sys
sys.stdin = open("input.txt")


# def dfs(elem, start, n):
#     if len(elem) == r:
#         global ans
#         ans += 1
#         return
#     for i in range(start, n):
#         elem.append(i)
#         dfs(elem, i+1, n)
#         elem.pop()


# def comb(n, r):
#     global ans
#     ans = 0
#     dfs([], 0, n)
#     return ans

# T = int(input())
# for tc in range(1, T+1):
#     n, r = map(int,input().split())
#     print((f"#{tc} {comb(n,r) % 1234567891}"))


# import itertools
# T = int(input())
# for tc in range(1, T+1):
#     n, r = map(int,input().split())
#     print(f"#{tc} {len(list(itertools.combinations(range(1,n+1), r))) % 1234567891}")

def cal_power(num, power):
    global mod

    if power == 0:
        return 1
    half = cal_power(num, power // 2) % mod

    if power % 2 == 0:
        return half * half % mod
    else:
        return num * half * half % mod


T = int(input())
fact = [0] * 1000001
fact[0] = 1
mod = 1234567891
for i in range(1, 1000001):
    fact[i] = (i * fact[i-1]) % mod

for tc in range(1, T+1):

    n, r = map(int,input().split())

    top = fact[n] % mod
    bottom = (fact[n-r] * fact[r])  % mod# 매우 큰 수 이다보니 수시로 나눠줌

    bottom = cal_power(bottom, mod-2) % mod

    ans = top * bottom % mod
    print(f"#{tc} {ans}")











