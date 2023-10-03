'''
LeetCode 901 : Online Stock Span
현재 주식 가격에서 더 작은 날짜를 가지고 있는 기간을 구하라.

'''
class StockSpanner:

    def __init__(self):
        self.stack = []
        
    def next(self, price: int) -> int:
        ans = 1
        while self.stack and self.stack[-1][0] <= price:
            ans += self.stack.pop()[1]
        self.stack.append([price, ans])
        return ans

s = StockSpanner()
# print(s.next(100))
# print(s.next(80))
# print(s.next(60))
# print(s.next(70))
# print(s.next(60))
# print(s.next(75))
# print(s.next(85))

print(s.next(100))
print(s.next(10))
print(s.next(20))
print(s.next(15))
print(s.next(20))







