class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
'''
leet : 117
주어진 bt에서 각 레벨당 node를 next로 이어라

# sol1 54ms 46% 17.5MB 96%
# O(n) O(n)
각 level을 배열로 저장하여 next로 연결함

# sol2 54ms 46% 17.6MB 96%
# O(n) O(1)
임시 temp를 만들어 현재 노드의 자식노드를 temp의 next로 연결한다.
그 이후에 root를 temp의 next로 이동하여 반복한다.

'''
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # sol1
        # arr = [root]
        # while arr:
        #     temp = []
        #     for node in arr:
        #         if node.left:
        #             temp.append(node.left)
        #         if node.right:
        #             temp.append(node.right)
        #     for i in range(len(temp)-1):
        #         temp[i].next = temp[i+1]
        #     arr = temp[:]
        # return root

        # sol2
        ret = root
        while root:
            temp = Node(0)
            child = temp
            while root:
                if root.left:
                    child.next = root.left
                    child = child.next
                if root.right:
                    child.next = root.right
                    child = child.next
                root = root.next
            root = temp.next
        return ret
    
        

    





        