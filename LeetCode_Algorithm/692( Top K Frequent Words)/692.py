from typing import List

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # sol1 85ms 51%
        # hashMap = {}
        # for string in words:
        #     if string not in hashMap:
        #         hashMap[string] = 1
        #     else:
        #         hashMap[string] += 1
        # temp = sorted(hashMap.items(), key = lambda item : item[0])
        # temp = sorted(temp, key = lambda item : item[1], reverse=True)

        # ans = []
        # for i in range(k):
        #     ans.append(temp[i][0])
        # return ans


        # sol2 93ms 39%
        # hashMap = {}
        # for word in words:
        #     hashMap[word] = hashMap.get(word, 0) + 1
    
        # ans = sorted(hashMap, key=lambda word:(-hashMap[word], word))
        # # 값과 똑같으면 word로 정렬
        # return ans[:k]

        # sol3 60ms 54% 14MB 18%
        import heapq
        hashMap = {}
        for word in words:
            hashMap[word] = hashMap.get(word, 0) + 1
        heap = []
        for (key, val) in hashMap.items():
            heapq.heappush(heap, (-val, key))
        
        return [heap[i][1] for i in range(k)]
        pass


print(Solution().topKFrequent(["i","love","leetcode","i","love","coding"], 3))