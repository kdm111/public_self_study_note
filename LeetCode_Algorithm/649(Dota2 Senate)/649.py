'''
R,D는 서로 경쟁 상대이다.
R은 다음에 오는 D를 한 번 무시할 수 있고
D는 다음에 오는 R을 한 번 무시할 수 있다.
R,D 중 승리하는 세력을 구하라.

# sol1 124ms 32% 16.9MB 7%
queue를 사용해야 한다.
세력은 뒤에 오는 다른 세력을 무시할 수 있다.
그리고 세력을 뒤에 추가한다.

'''
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r = []; q = []
        for i in range(len(senate)):
            if senate[i] == 'R':
                r.append(i)
            else:
                q.append(i)
        while r and q:
            i = r.pop(0)
            j = q.pop(0)
            if i < j:
                r.append(i + len(senate))
            else:
                q.append(j + len(senate))
        return "Radiant" if r else "Dire"
            
                

print(Solution().predictPartyVictory("RDD"))