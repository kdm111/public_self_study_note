_ = input()
inp = list(map(int, input().split(" ")))
k = int(input())
from collections import defaultdict
d = defaultdict(int)
for c in inp:
    d[c] += 1
print(d.get(k) or 0)