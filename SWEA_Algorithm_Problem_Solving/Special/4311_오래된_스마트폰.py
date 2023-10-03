

# 배열

# 1부터 10 까지 출력해보라
# for i in range(1, 11):
#   print(i, end= " ")

# 너무나도 쉽다.

# 이와 같이 알고리즘의 기본기도 이렇게 되어야 한다.
# 기본기가 숙달 될 때 까지 공부를 해야 한다.

# 능숙함의 차이
# 쉬운 문제를 많이 풀 수록 쉽게 문제를 풀 수 있다.


# 정올 - 주사위 던지기1


# def solve1(k, arr):
#     global N, ans
#     if N == k:
#         print(*arr)
#         return

#     for i in range(1,7):
#         arr.append(i)
#         solve1(k+1, arr)
#         arr.pop()

# def solve2(k, arr):
#     global N, ans
#     if N == k:
#         print(*arr)
#         return
#     for i in range(1,7):
#         if len(arr) > 0 and arr[-1] <= i:
#             arr.append(i)
#             solve2(k+1, arr)
#             arr.pop()
#         elif len(arr) == 0:
#             arr.append(i)
#             solve2(k+1, arr)
#             arr.pop()

# def solve3(k, arr):
#     global N, ans
#     if N == k:
#         print(*arr)
#         return
#     for i in range(1,7):
#         if i in arr: continue;
#         arr.append(i)
#         solve3(k+1, arr)
#         arr.pop()

# N, M = map(int, input().split())
# ans = []
# if M == 1: solve1(0, []); 
# elif M == 2: solve2(0, []); 
# else: solve3(0, []);


# 가지 치기


# def run(lev):

#     # if (lev == 1) and (arr[0] != 7 or arr[0] != 9): return;


#     if lev == n:
#         print(*arr)
#         return

#     for i in range(1,10):
#         # for 문 안에서도 가지치기가 될 수 있다.
#         arr.append(i)
#         if (lev == 1) and (arr[0] == 7 or arr[0] == 9): continue;
#         run(lev+1)
#         arr.pop()

# n = 2

# arr= []
# run(0)


# 가지 치기는 함수의 위에서 하는 것과 아래에서 하는 것이 있다.

# 위에서 가지치기 하는 것은 1로 들어가 잘못들어가면 바로 나온다.


# 오래된 스마트폰

# A형 문제는 문제가 비슷한데 B형 에서 삼성 전자는 A형의 업그레이드 형태로 나온다.


# 브랜치가 연산자 수 * 만들어 질 수 있는 수의 갯수

# 타인의 코드를 이해하는 작업은 노력이 많이 필요하다.
# 의도를 알고 이해를 한다. 이 과정은 굉장히 힘들다.
# 단계를 나눠서 생각하고
# 설계를 한다.
#

