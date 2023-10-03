
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def lowestCommonAncestor(self,tree, p: 'Node', q: 'Node') -> 'Node':
        root = self.makeTree(tree, 0, None)

        # 모든 밸류는 유니크하다.
        stack = [root]
        p_node, q_node = None, None;
        # level traversal
        while p_node == None or q_node == None:
            node = stack.pop(0)
            if node.val == p:
                p_node = node
            if node.val == q:
                q_node = node
            stack.append(node.left)
            stack.append(node.right)

        # sol1 만날 때까지 계속 돌림 169ms 5%
        # s = p_node
        # t = q_node
        # while s != t:
        #     print(s.val, t.val)
        #     s = q_node if s.parent == None else s.parent
        #     t = p_node if t.parent == None else t.parent
        # return s.val

        # sol2 visited 스택 사용 128ms 18%
        s = p_node
        t = q_node
        visited = []
        while s:
            visited.append(s)
            s = s.parent
        while t:
            if t in visited:
                return t.val
            t = t.parent
            
    def makeTree(self,leaf, idx, parent):
        rootNode = Node(leaf[idx])
        if parent is not None: rootNode.parent = parent
        if 2*idx+1 < len(leaf): rootNode.left = self.makeTree(leaf, 2*idx+1, rootNode)
        if 2*idx+2 < len(leaf): rootNode.right = self.makeTree(leaf, 2*idx+2, rootNode)
        return rootNode

print(Solution().lowestCommonAncestor([3,5,1,6,2,0,8,None,None,7,4], 5, 4))