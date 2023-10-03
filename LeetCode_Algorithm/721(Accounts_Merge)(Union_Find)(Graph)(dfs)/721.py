from typing import List
from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # sol1 5716ms 5%
        name_of_email = {}
        email_graph = defaultdict(set)
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                # 상호 그래프 연결
                email_graph[account[1]].add(email)
                email_graph[email].add(account[1])
                # 그래프와 소유주 연결
                name_of_email[email] = name
                
        ans = []; visited = []
        for email in email_graph:
            if email not in visited:
                visited.append(email)
                name = name_of_email[email]
                temp = [email]; emails = []
                while temp:
                    email = temp.pop()
                    emails.append(email)
                    for e in email_graph[email]:
                        if e not in visited:
                            temp.append(e)
                            visited.append(e)
                ans.append([name] + sorted(emails))
        return ans

print(Solution().accountsMerge([["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]))
# print(Solution().accountsMerge([["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]))
