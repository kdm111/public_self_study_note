import sys
sys.stdin = open("input.txt")


import sys
def burble_sorting(string): # 버블 소트 해봤는 데 시간초과 최대 1000글자 3초 이내 문제.
    for i in range(len(string)):
        for j in range(len(string)-1, i, -1):
            if string[i] < string[j]:
                string[i], string[j] = string[j], string[i]
    return string


def merge_sorting(string):
    if len(string) == 1:
        return string
    
    mid = len(string)//2
    left = string[:mid]
    right = string[mid:]

    left_sorted = merge_sorting(left)
    right_sorted = merge_sorting(right)

    string_sorted = []
    idx_l, idx_r = 0, 0

    while idx_l < len(left_sorted) or idx_r < len(right_sorted):
        if idx_l == len(left_sorted):
            string_sorted.append(right_sorted[idx_r]); idx_r += 1; continue;

        if idx_r == len(right_sorted):
            string_sorted.append(left_sorted[idx_l]); idx_l += 1; continue;

        if left_sorted[idx_l] <= right_sorted[idx_r]:
            string_sorted.append(left_sorted[idx_l]); idx_l += 1;
        else:
            string_sorted.append(right_sorted[idx_r]); idx_r += 1;

    return string_sorted


def solve(string1, string2):
    # string1_sorted = burble_sorting(list(string1))
    # string2_sorted = burble_sorting(list(string2))

    string1_sorted = merge_sorting(list(string1))
    string2_sorted = merge_sorting(list(string2))

    for i in range(len(string1_sorted)):
        if string1_sorted[i] != string2_sorted[i]:
            return "different"
    return "same"

k = 0
while True:
    string1 = sys.stdin.readline().strip()
    string2 = sys.stdin.readline().strip()
    if string1 == "END" and string2 == "END":
        break
    k += 1
    if len(string1) != len(string2):
        print(f"Case {k}: different")
    else:
        print(f"Case {k}: {solve(string1, string2)}")
        
    

    # if len(string1) != len(string2):
    #     print(f"Case {i}: different")
    # else:
    #     print(f"Case {i}: {solve(string1, string2)}")


# ANS
# k = 0
# while True:
#     string1 = input()
#     string2 = input()
#     if string1 == "END" and string2 == "END":
#         break

#     x = sorted(list(string1))
#     y = sorted(list(string2))
#     flag = 0
#     k += 1
#     if len(x) != len(y):
#         print(f"Case {k}: different")
#         flag = 1
    
#     if flag != 1:
#         for i in range(len(x)):
#             if x[i] != y[i]:
#                 print(f"Case {k}: different")
#                 flag = 1
#                 break
#     if flag == 0:
#         print(f"Case {k}: same")
    



