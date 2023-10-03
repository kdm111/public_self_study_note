import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):

    N, M, K = map(int, input().split())
    customer = sorted(list(map(int,input().split())))

    sec = 0
    bread = 0
    while sec <= customer[-1]:
        if M <= sec and sec % M == 0:
            bread += K
        if sec in customer:
             bread -= 1
        if bread < 0:
            break
        sec += 1
        
    print(f"#{tc} Possible") if bread >= 0 else print(f"#{tc} Impossible")