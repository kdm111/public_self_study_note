# class MinStack:
#     # 일반 스택처럼 행동하되 getMin을 O(1)으로 동작하게 해야함
#     # 스택 lst, min_lst 사용 
#     # sol1 96ms 55%
#     def __init__(self):
#         self.lst = []
#         # O(1)을 가지기 위한 리스트
#         self.min_lst = []
        
#     def push(self, val: int) -> None:
#         self.lst.append(val)
#         if len(self.min_lst) == 0:
#             self.min_lst.append(val)
#         else:
#             if self.min_lst[-1] >= val:
#                 # =은 중복을 위해서
#                 self.min_lst.append(val)        
#     def pop(self) -> None:
#         if self.lst[-1] == self.min_lst[-1]:
#             self.min_lst.pop()
#         self.lst.pop()
#     def top(self) -> int:
#         return self.lst[-1]
#     def getMin(self) -> int:
#         return self.min_lst[-1]


class MinStack:

    # 스택 1개만
    # sol2 51ms 99% 20.7MB 15%
    def __init__(self):
        self.lst = []
        
    def push(self, val: int) -> None:
        # 첫 번째로 있는 val은 항상 들어오는 val을 유지
        # 두 번째 요소는 항상 min 값을 유지
        if len(self.lst) == 0:
            self.lst.append((val, val))
        else:
            if self.lst[-1][1] < val:
                self.lst.append((val, self.lst[-1][1]))
            else:
                self.lst.append((val, val))
    def pop(self) -> None:
        self.lst.pop()
    def top(self) -> int:
        return self.lst[-1][0]
    def getMin(self) -> int:
        return self.lst[-1][1]
