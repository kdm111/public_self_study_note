
import sys
sys.stdin = open('input.txt')


heights = [int(input()) for _ in range(9)]

total = sum(heights)
heights.sort()
flag = 0
for i in range(8):
    for j in range(i+1,9):
        if total-(heights[i]+heights[j]) == 100:
            flag = 1
            break
    if flag == 1:
        break
        

for k in range(len(heights)):
    if k != i and k != j:
        print(heights[k])

