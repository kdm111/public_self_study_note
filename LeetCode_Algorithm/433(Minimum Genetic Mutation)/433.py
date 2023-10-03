'''
LeetCode 433 : Minimum Genetic Mutation

'''
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        # sol1 51ms 5% 13.9MB 77%
        if endGene not in bank:
            return -1
        graph = {
            'A' : ['C', 'G', 'T'],
            'C' : ['A', 'G', 'T'],
            'G' : ['A', 'C', 'T'],
            'T' : ['A', 'C', 'G']
        }
        from collections import deque
        queue = deque([(startGene, 0)])
        seen = set([startGene])
        while queue:
            gene, cnt = queue.popleft()
            if gene == endGene:
                return cnt
            for i in range(8):
                for c in graph[gene[i]]:
                    newGene = gene[:i] + c + gene[i+1:]
                    if newGene in bank and newGene not in seen:
                        seen.add(newGene)
                        queue.append((newGene, cnt+1))
        return -1