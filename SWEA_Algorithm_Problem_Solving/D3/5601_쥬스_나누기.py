import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    print(f"#{tc}",end=" ")
    for _ in range(n):
        print(f"1/{n}", end=" ")
    print()