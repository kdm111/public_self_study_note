'''
# 완탐
'''
def solution(users, emoticons):
    ans = [-1, -1]
    def getAllPossibleEmoticons(i, temp):
        if i == len(emoticons):
            possibleEmoticons.append(temp[:])
            return ;
        for v in [9,8,7,6]:
            temp.append(((10 - v) * 10, emoticons[i] * v // 10))
            getAllPossibleEmoticons(i+1, temp)
            temp.pop()
    possibleEmoticons = []
    getAllPossibleEmoticons(0, [])

    for emoticon in possibleEmoticons:
        revenue = 0; plusUser = 0
        for user in users:
            temp = user[:]; temp_revenue = 0
            for emo in emoticon:
                if temp[0] <= emo[0]:
                    temp[1] -= emo[1]; 
                    temp_revenue += emo[1]
                    if temp[1] <= 0:
                        plusUser += 1
                        temp_revenue = 0
                        break
            revenue += temp_revenue
        if plusUser > ans[0]:
            ans = [plusUser, revenue]
        elif plusUser == ans[0]:
            ans[1] = max(ans[1], revenue)
    return ans

            

print(solution([[40, 10000], [25, 10000]], 	[7000, 9000]))
print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], \
                [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]))
