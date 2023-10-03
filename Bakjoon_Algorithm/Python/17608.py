import sys

n = int(sys.stdin.readline())

bars = []
for _ in range(n):
    bars.append(int(sys.stdin.readline()))

ans = 0 
k = bars[-1]
for i in range(len(bars)-1, -1, -1):
    if bars[i] > k:
        ans += 1
        k = bars[i]
print(ans+1)