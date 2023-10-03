class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        # sol1 25ms 99.4%
        # datetime 모듈 사용
        from datetime import date
        date1 = list(map(int, date1.split("-")))
        date2 = list(map(int, date2.split("-")))
        
        # date 클래스 사용
        date1 = date(date1[0], date1[1], date1[2])
        date2 = date(date2[0], date2[1], date2[2])
        # 빼주고
        delta = date1-date2

        # 뺀 나머지에서 날짜를 뽑아내면 종료
        return (abs(delta.days))

                
        # 왜 이런 문제가 주어졌을까?
        # api를 호출하지 않기로 마음 먹었다면 인터뷰 중에 시간을 잃게 된다.
        # 그렇게 하지 않으면 1971년 부터 날짜를 전부다 계산하고
        # 윤년 (year % 4 == 0 ) and (year % 100 != 0 or year % 1000 == 0)
        # 을 계산하고 31,28,31,30,31,30,31,31,30,31,30,31,31이런 날짜를 넣어서 계산해야 한다.
        

print(Solution().daysBetweenDates("2020-01-15", "2019-12-31"))

print(Solution().daysBetweenDates("2020-01-15", "2020-01-31"))
print(Solution().daysBetweenDates("2020-02-15", "2020-01-21"))

