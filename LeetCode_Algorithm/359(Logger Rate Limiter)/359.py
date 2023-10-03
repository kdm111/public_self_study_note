'''
LeetCode 359 : Logger Rate Limiter
로거 시스템을 디자인해보라.
각각의 메시지는 최대 10초마다 인쇄되어야 한다.
타임스탬스 t에 인쇄된 메시지는 다른 동일한 메시지가 타임스탬프까지 인쇄되지 않도록 한다.

# sol1 393ms 16% 20.9MB 36%
O(1) O(n) 
해쉬맵으로 저장한 뒤 타임스탬프를 찍어놓음

'''
class Logger:

    def __init__(self):
        self.hashMap = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.hashMap:
            self.hashMap[message] = timestamp + 10
            return True
        else:
            if timestamp < self.hashMap[message]:
                return False
            else:
                self.hashMap[message] = timestamp + 10
                return True