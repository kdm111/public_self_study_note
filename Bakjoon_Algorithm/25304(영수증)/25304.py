total = int(input())
temp = 0
for _ in range(int(input())):
    a, b = map(int, input().split(" "))
    temp += (a * b)

print("Yes") if total == temp else print("No")

    