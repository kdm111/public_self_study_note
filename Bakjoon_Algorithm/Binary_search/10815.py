# https://www.acmicpc.net/problem/10815


# import os
# f  = open(os.path.expanduser("~/Desktop/Self_study_note/baekjoon/Binary_search/input.txt"))

import sys
sys.stdin = open("input.txt")

# 시간 초과
def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while (left<=right):
        pivot = (left + right) // 2
        if (nums[pivot] == target):
            print("1", end=" ")
            return

        elif (nums[pivot] < target):
            left = pivot + 1
        else:
            right = pivot - 1
    print("0", end=" ")
    return


card_num = int(sys.stdin.readline().strip())
card_list  = list(map(int, sys.stdin.readline().strip().split()))
target_num = int(sys.stdin.readline().strip())
target_list = list(map(int, sys.stdin.readline().strip().split()))

# card_list = list(set(card_list)).sort()
# card_list.sort()
# for i in target_list:
    # binary_search(card_list, i)


# 이진 탐색은 정렬된 배열이 필요하다. 
# 배열을 정렬하면서 퀵 소트는 nlogn의 시간 복잡도를 가지고 이진 탐색은 nlogn의 시간 복잡도를 가지므로
# (m+n)logn의 시간복잡도를 가지게 된다.
# 그래서 set을 활용한 풀이 방법이 정답이 나온다고 쓰여 있어서 한 번 써 보았다.

def solve(nums, targets):
    nums = set(nums)

    for i in targets:
        if i in nums:
            print("1", end=" ")
        else:
            print("0", end=" ")

solve(card_list, target_list)

# 668ms로 정답이 나오기는 했다.
# set을 활용하여 in을 통하면 O(1)의 시간 복잡도를 가진다.
# targets의 길이 O(n)의 시간 복잡도로 문제를 해결하였다.

