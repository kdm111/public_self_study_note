from typing import List

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:

        # sol1 132~180ms 21~5%
        hashMap = {}
        for [key, value] in items:
            if key not in hashMap:
                hashMap[key] = [value]
            else:
                if len(hashMap[key]) >= 5:
                    hashMap[key].sort(reverse=True)
                    if hashMap[key][4] < value:
                        hashMap[key][4] = value
                else:
                    hashMap[key].append(value)

        for key in hashMap:
            hashMap[key] = int(sum(hashMap[key]) / 5)
        hashMap = sorted(hashMap.items(), key = lambda x: x[0])
        ret = []
        for (key, value) in hashMap:
            ret.append([key, value])
        return ret


print(Solution().highFive([[5,91],[5,92],[3,93],[3,97],[5,60],[3,77],[5,65],[5,87],[5,100],[3,100],[3,76]]))