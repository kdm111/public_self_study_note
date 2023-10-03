import sys
sys.stdin = open("test.txt", 'r')
m , n  = map(int ,input().split(" "))
k = int(input())
n += k
if n >= 60:
    m += n // 60
    n %= 60

    if m >= 24:
        m %= 24
print(m, n)

