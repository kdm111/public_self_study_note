'''
leetCode 933 
RecentCounter 클래스는 
0번의 요청 수로 초기화 한다.
ping 메소드에서는 시간 t에서 요청이 추가된다. t의 단위는 밀리초이다.
이전 3000밀리초의 요청을 리턴하라. [t-3000, t]
ping에서 t는 항상 이전의 t보다 크다.

# sol1
266ms 75% 21.66MB 48%
t는 항상 커지므로 큐를 통해 계산한다.

'''
class RecentCounter:

    def __init__(self):
        self.queue = []

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while self.queue[0] < t-3000:
            self.queue.pop(0)
        return len(self.queue)

        