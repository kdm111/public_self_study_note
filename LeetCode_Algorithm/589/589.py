from typing import List
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = []

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # O(n) 56ms 89%
        rootnode = Node(1)
        a_node = Node(2); b_node = Node(3); c_node = Node(4)
        rootnode.children.append(a_node);
        rootnode.children.append(b_node);
        rootnode.children.append(c_node);
        return self.solve(rootnode, [])

    def solve(self, root, ans):
        if not root:
            return ans
        ans.append(root.val)
        for child in root.children:
            self.solve(child, ans)
        return ans
        
        

        
        

            
            

print(Solution().preorder([1,None,3,2,4,None,5,6]))