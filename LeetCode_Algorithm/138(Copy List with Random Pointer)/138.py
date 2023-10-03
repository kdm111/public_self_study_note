'''
LeetCode 138 : Copy List with Random Pointer
주어진 링크드 리스트를 딥카피 하라. 그 어떤 포인터도 원본을 가리키면 안된다.

# sol1 43ms 65% 15MB 42%
O(n) O(n)
딕셔너리의 키로 노드를 사용하여 문제를 해결한다.
노드에 딕셔너리의 키로 노드를 사용하여 차례로 대입한 뒤 계속해서 진행시켜 문제를 해결
js에서 해쉬맵에서 키가 안 먹는다.
'''
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

from typing import Optional
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        self.visited = {}

        init = head
        newNode = Node(head.val)
        self.visited[head] = newNode
        while head:
            newNode.random = self.getNode(head.random)
            newNode.next = self.getNode(head.next)
            head = head.next
            newNode = newNode.next
        return self.visited[init]

    def getNode(self, node):
        if node:
            if node not in self.visited:
                self.visited[node] = Node(node.val)
            return self.visited[node]
        else:
            return None