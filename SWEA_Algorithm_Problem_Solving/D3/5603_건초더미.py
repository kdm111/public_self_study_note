import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    inp = []
    for _ in range(n):
        inp.append(int(input()))
    
    avg = sum(inp) // n
    total = 0
    for i in range(n):
        total += abs(avg-inp[i])
    print(f"#{tc} {total // 2}")
    
    