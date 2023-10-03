import sys
sys.stdin = open('test.txt', 'r')

for _ in range(int(sys.stdin.readline())):
    inputs = []
    for _ in range(int(sys.stdin.readline())):
        inputs.append(sys.stdin.readline().strip())
    inputs.sort()
    flag = True
    for i in range(len(inputs)-1):
        if inputs[i] == inputs[i + 1][0: len(inputs[i])]:
            flag = False
            print('NO')
            break
    if flag:
        print('YES')