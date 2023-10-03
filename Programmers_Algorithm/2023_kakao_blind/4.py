def solution(numbers):
    answer = []
    for number in numbers:
        if solve(number):
            answer.append(1)
        else:
            answer.append(0)
    return answer

def solve(number):
    num = "".join(bin(number)[2:])
    if num.count('1') == 1:
        return True
    i = 1
    while 2 ** (i - 1) - 1 < len(num):
        i += 1
    while 2 ** (i - 1) - 1 > len(num):
        num = '0' + num
    l, r = 0, len(num)-1; m = (l + r) // 2
    queue = [(l, r, num[m] == '1')]
    if num[m] != '1':
        return False
    while queue:
        l, r, curr = queue.pop(0)
        if l > r: continue
        m = (l + r) // 2
        if curr == False and num[m] == '1':
            return False
        queue.append((l, m-1, num[m] == '1'))
        queue.append((m+1, r, num[m] == '1'))
    return True

'''
루트에서 시작해서 top-down으로 내려가면서 경로를 계산하여 0이 나와야 하는 지 1이 나와야 하는지 계산
'''


# print(solution([7, 42, 5, 16]))
# print(solution([63,111,95]))
print(solution([95]))

