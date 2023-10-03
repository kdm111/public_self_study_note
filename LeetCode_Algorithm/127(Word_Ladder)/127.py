from typing import List
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if not beginWord or not endWord or not wordList:
            return 0
        if endWord not in wordList:
            return 0
        # sol1 4941 5%
        # graph를 그려서 가능한 모든 값에 key를 매핑하고 word를 매핑한다.
        # graph = {};
        # for word in wordList:
        #     for idx in range(len(word)):
        #         temp = list(word); temp[idx] = "_"
        #         key = ''.join(temp)
        #         if key not in graph:
        #             graph[key] = [word]
        #         else:
        #             graph[key].append(word)
        # # bfs로 찾아가면서 목표에 도달하면 cnt+1 아니면 계속 루프
        # from collections import deque
        # queue = deque([(beginWord, 0)]); visited = []
        # while queue:
        #     word, cnt = queue.popleft()
        #     if word == endWord:
        #         return cnt+1
        #     if word in visited:
        #         continue
        #     visited.append(word)
        #     for idx in range(len(word)):
        #         temp = list(word); temp[idx] = "_"
        #         key = ''.join(temp)
        #         if graph.get(key):
        #             for word_key in graph[key]:
        #                 queue.append((word_key, cnt+1))
        # return 0

        # sol2 126ms 91% 18.4MB 19%
        from collections import defaultdict, deque
        graph = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                key = word[:i] + '*' + word[i+1:]
                graph[key].append(word)
        queue = deque([(beginWord, 1)]); seen = set([beginWord])
        while queue:
            word, cnt = queue.popleft()

            if word == endWord:
                return cnt
            for i in range(len(word)):
                key = word[:i] + '*' + word[i+1:]
                for w in graph[key]:
                    if w not in seen:
                        seen.add(w)
                        queue.append((w, cnt+1))
                graph[key] = []
        return 0

        
print(Solution().ladderLength("a", "c", ["a", "b", "c"]))