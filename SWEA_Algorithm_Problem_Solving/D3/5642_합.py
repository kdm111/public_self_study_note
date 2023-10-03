#https://shoark7.github.io/programming/algorithm/4-ways-to-get-subarray-consecutive-sum

# 카데인 알고리즘


import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    _ = input()
    inp = list(map(int,input().split()))
    
    current_sum = inp[0]
    max_sum = inp[0]
    for i in range(1, len(inp)):
        current_sum = current_sum + inp[i] if inp[i] < current_sum + inp[i] else inp[i]
        max_sum = current_sum if max_sum < current_sum else max_sum

    print(f"#{tc} {max_sum}")


