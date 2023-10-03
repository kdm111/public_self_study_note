'''
LeetCode 993 : Cousins in Binary Tree
트리의 각 노드는 서로 독립적인 값을 가지고 있으며 
같은 깊이에서 다른 부모 노드를 가지고 있으면 true를 리턴하라.

# sol1 28ms 93% 13.9MB 40%
x,y가 이미 트리에 존재하고 각각 유니크하므로 그 부모를 찾아서 같은 레벨과 다른 밸류를 가지는 지 확인한다.

'''
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        queue = [(root, 0)]
        par_x = [-1, -1]; par_y = [-1, -1]
        left = right = False
        while queue:
            node, level = queue.pop(0)
            if node.left:
                if node.left.val == x:
                    par_x = [level, node.val]
                    left = True
                if node.left.val == y:
                    par_y = [level, node.val]
                    left = True
                queue.append((node.left, level + 1))
                
            if node.right:
                if node.right.val == x:
                    par_x = [level, node.val]
                    right = True
                if node.right.val == y:
                    par_y = [level, node.val]
                    right = True
                queue.append((node.right, level + 1))
                    
            if left and right:
                break
        if par_x[0] == par_y[0] and par_x[1] != par_y[1]:
            return True
        return False
