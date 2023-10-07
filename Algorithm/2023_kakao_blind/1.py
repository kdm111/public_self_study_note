'''

고객의 약관 동의를 얻어서 수집된 1~n번으로 분류되는 개인정보 n개가 있습니다. 
약관 종류는 여러 가지 있으며 각 약관마다 개인정보 보관 유효기간이 정해져 있습니다. 
당신은 각 개인정보가 어떤 약관으로 수집됐는지 알고 있습니다. 
수집된 개인정보는 유효기간 전까지만 보관 가능하며, 
유효기간이 지났다면 반드시 파기해야 합니다.

예를 들어, A라는 약관의 유효기간이 12 달이고, 
2021년 1월 5일에 수집된 개인정보가 A약관으로 수집되었다면 
해당 개인정보는 2022년 1월 4일까지 보관 가능하며 2022년 1월 5일부터 파기해야 할 개인정보입니다.
당신은 오늘 날짜로 파기해야 할 개인정보 번호들을 구하려 합니다.

모든 달은 28일까지 있다고 가정합니다.
'''
def toNumber(string):
    ret = 0
    for c in string:
        if c != '0' or c != ' ':
            ret *= 10
            ret += int(c)
    return ret
def solution(today, terms, privacies):
    answer = []
    today = list(map(toNumber, today.split('.')))
    today_date = 12 * 28 * (today[0]-1) + 28 * (today[1]-1) + today[2]
    t = {}
    for term in terms:
        term = term.split(' ')
        t[term[0]] = int(term[1])
    idx = 1
    for privacy in privacies:
        privacy = privacy.split(' ')
        day = list(map(toNumber, privacy[0].split('.')))
        reg = privacy[1]
        privacy_date = 12 * 28 * (day[0]-1) + 28 * (day[1]-1) + day[2]
        privacy_date += t[reg] * 28
        if today_date >= privacy_date:
            answer.append(idx)
        idx += 1
    return answer

print(solution("2022.05.19", \
               ["A 6", "B 12", "C 3"], \
               ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))


print(solution("2020.01.01", \
               ["Z 3", "D 5"], \
               ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))
print(solution("2021.05.15", \
               ["A 1", "B 18"], \
               ["2000.12.01 A", "2019.10.15 B"]))