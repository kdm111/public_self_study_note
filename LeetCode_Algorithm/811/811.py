from typing import List
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        # sol1 118ms 6%
        hashMap = {}
        for cpdomain in cpdomains:
            count, domain = cpdomain.split(' ')
            parts = domain.split('.')
            for idx in range(len(parts)-1, -1, -1):
                temp = ""
                for part in parts[idx:]:
                    temp += part
                    temp += '.'
                if temp[:len(temp)-1] not in hashMap:
                    hashMap[temp[:len(temp)-1]] = int(count)
                else:
                    hashMap[temp[:len(temp)-1]] += int(count)

        ans = []
        for domain, count in hashMap.items():
            temp = str(count) + ' ' + domain
            ans.append(temp)
        return ans
            


print(Solution().subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))
# print(Solution().subdomainVisits(["1 intel.mail.com"]))
