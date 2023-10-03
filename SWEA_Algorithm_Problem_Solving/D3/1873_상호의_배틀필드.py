import sys
sys.stdin = open("input.txt", "r")


T = int(input())
for tc in range(1, T+1):
    H, W = map(int,input().split())
    BRD = []
    for _ in range(H):
        BRD.append(list(input()))
    
    for r in range(H):
        for c in range(W):
            if BRD[r][c] == "<" or BRD[r][c] == ">" or BRD[r][c] == "^" or BRD[r][c] == "v":
                R = r
                C = c
                break
    _ = input()
    command = list(input())
    for char in command:
        pos = BRD[R][C]
        # print("{}".format("".join(BRD[0])))
        # for i in range(1, H):
        #     print("{}".format("".join(BRD[i])))
        # print()
        if char == "U":
            if  0 <= R-1 and BRD[R-1][C] == ".":
                R -= 1
                BRD[R+1][C] = "."
                BRD[R][C] = "^"   
            else:
                BRD[R][C] = "^"   
        elif char == "D":
            if R + 1 < H and BRD[R+1][C] == ".":
                R += 1
                BRD[R-1][C] = "."
                BRD[R][C] = "v"   
            else    : 
                BRD[R][C] = "v"   
        elif char =="R":
            if  C + 1 < W and BRD[R][C+1] == ".":
                C += 1
                BRD[R][C-1] = "."
                BRD[R][C] = ">"   
            else    : 
                BRD[R][C] = ">"   
        elif char == "L":
            if 0 <= C - 1 and BRD[R][C-1] == ".":
                C -= 1
                BRD[R][C+1] = "."
                BRD[R][C] = "<"   
            else    : 
                BRD[R][C] = "<" 

        elif char == "S":
            if pos == "^":
                for r in range(R, -1, -1):
                    if BRD[r][C] == "*":
                        BRD[r][C] = "."
                        break
                    elif BRD[r][C] == "#":
                        break         
            elif pos ==  "v":
                for r in range(R, H):
                    if BRD[r][C] == "*":
                        BRD[r][C] = "."
                        break
                    elif BRD[r][C] == "#":
                        break
            elif pos == ">":
                for c in range(C, W):
                    if BRD[R][c] == "*":
                        BRD[R][c] = "."
                        break
                    elif BRD[R][c] == "#":
                        break
            elif pos == "<":
                for c in range(C, -1, -1):
                    if BRD[R][c] == "*":
                        BRD[R][c] = "."
                        break
                    elif BRD[R][c] == "#":
                        break
        else:
            pass
    print("#{} {}".format(tc, "".join(BRD[0])))
    for i in range(1, H):
        print("{}".format("".join(BRD[i])))

