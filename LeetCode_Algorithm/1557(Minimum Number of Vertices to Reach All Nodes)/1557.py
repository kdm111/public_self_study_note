'''
LeetCode 1557 : Minimum Number of Vertices to Reach All Nodes
유향 비순환 그래프가 주어졌을 때 모든 노드를 순회하고자 할때 
도달할 수 없는 노드들의 set을 리턴하라.

# sol1 1190ms 73% 52.7MB 31%
모든 노드를 셋에 저장한뒤 
incoming node를 셋에서 뺀다.
'''

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: list[list[int]]) -> list[int]:
        nodes = set([i for i in range(n)])
        for [_, node] in edges:
            if node in nodes:
                nodes.remove(node)
        return list(nodes)